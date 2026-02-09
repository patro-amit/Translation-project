import easyocr
import whisper
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer # Added AutoTokenizer
import os
from langdetect import detect
import time # Added for retry logic in get_translation_pipeline
import http.client # Added for retry logic in get_translation_pipeline
import warnings
import logging

# Suppress FutureWarnings from torch.load
warnings.filterwarnings('ignore', category=FutureWarning, module='whisper')

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

OCR_READER = None
WHISPER_MODEL = None
TRANSLATION_PIPELINES = {} # Cache for pipelines {pipe_key: pipeline_object}
TOKENIZERS = {} # Cache for tokenizers {model_name: tokenizer_object}

SUPPORTED_LANGUAGES = {
    # Friendly Name : NLLB Code
    "Assamese": "asm_Beng",
    "Bengali": "ben_Beng",
    "Gujarati": "guj_Gujr",
    "Hindi": "hin_Deva",
    "Kannada": "kan_Knda",
    "Malayalam": "mal_Mlym",
    "Marathi": "mar_Deva",
    "Odia": "ory_Orya",
    "Punjabi": "pan_Guru",
    "Tamil": "tam_Taml",
    "Telugu": "tel_Telu",
    "Urdu": "urd_Arab",
}
NLLB_SOURCE_LANG_CODES = {
    # Short Code : NLLB Code
    "en": "eng_Latn",
    "hi": "hin_Deva"
}

# This map seems unused in the current code, but keeping it just in case
ISO_TO_NLLB = {
    'as': 'asm_Beng',
    'bn': 'ben_Beng',
    'gu': 'guj_Gujr',
    'hi': 'hin_Deva',
    'kn': 'kan_Knda',
    'ml': 'mal_Mlym',
    'mr': 'mar_Deva',
    'or': 'ory_Orya',
    'pa': 'pan_Guru',
    'ta': 'tam_Taml',
    'te': 'tel_Telu',
    'ur': 'urd_Arab',
    'en': 'eng_Latn',
}

def initialize_models():
    global OCR_READER, WHISPER_MODEL
    logging.info("Initializing EasyOCR reader...")
    OCR_READER = easyocr.Reader(['en', 'hi'], gpu=False)
    logging.info("EasyOCR reader initialized.")

    logging.info("Loading Whisper model (base)...")
    WHISPER_MODEL = whisper.load_model("base")
    logging.info("Whisper model loaded.")

def get_easyocr_reader(lang_code):
    """Get EasyOCR reader for specific language scripts."""
    supported_scripts = ['en', 'hi', 'mr', 'ne']
    if lang_code in ['ta', 'te', 'kn', 'ml', 'bn', 'as', 'gu', 'pa', 'ur', 'or']:
        langs_to_load = [lang_code, 'en']
        logging.debug(f"Initializing EasyOCR for specific script: {langs_to_load}")
        return easyocr.Reader(langs_to_load, gpu=False)
    else:
        logging.debug(f"Initializing EasyOCR for default scripts: {supported_scripts}")
        return easyocr.Reader(supported_scripts, gpu=False)


def perform_ocr(image_path, lang_code='en'):
    """Perform OCR on image and detect language."""
    logging.debug(f"Performing OCR on: {image_path} (Hint: {lang_code})")
    
    if OCR_READER is None:
        logging.error("Global EasyOCR reader not initialized!")
        reader = easyocr.Reader(['en','hi'], gpu=False)
    else:
        reader = OCR_READER

    try:
        result = reader.readtext(image_path, detail=0, paragraph=True)
        # Handle both string results and list results from EasyOCR
        if isinstance(result, list):
            text = " ".join(str(item) for item in result)
        else:
            text = str(result)
        logging.debug(f"OCR Raw Text: {text[:100]}...")
    except Exception as ocr_err:
        logging.error(f"EasyOCR readtext failed: {ocr_err}")
        text = ""

    detected_lang = 'en'
    if text:
        try:
            detected_lang = detect(text)
            logging.debug(f"Langdetect on OCR text: {detected_lang}")
        except Exception as detect_err:
            logging.warning(f"Langdetect failed on OCR text: {detect_err}, defaulting to 'en'.")
            detected_lang = 'en'
    else:
        logging.warning("OCR produced no text, defaulting lang to 'en'.")

    return text, detected_lang

def perform_stt(audio_path, lang_code_hint=None):
    """Perform speech-to-text using Whisper model."""
    global WHISPER_MODEL
    if WHISPER_MODEL is None:
        logging.error("Whisper model is None in perform_stt!")
        raise Exception("Whisper model not initialized.")
    try:
        logging.debug(f"Starting Whisper transcription for: {audio_path}")
        if lang_code_hint:
            logging.debug(f"Forcing Whisper language: {lang_code_hint}")
            result = WHISPER_MODEL.transcribe(audio_path, fp16=False, language=lang_code_hint)
        else:
            result = WHISPER_MODEL.transcribe(audio_path, fp16=False)
        text = result['text']
        lang_short = result['language']
        logging.debug(f"Whisper transcription successful. Lang='{lang_short}', Text='{text[:100]}...'")
        return text, lang_short
    except Exception as e:
        logging.error(f"Error during STT transcription: {e}")
        import traceback
        traceback.print_exc()
        return None, None
def detect_language(text):
    """Detect language of input text."""
    if not text:
        return "unknown"
    try:
        lang = detect(text)
        logging.debug(f"Langdetect on input text: {lang}")
        return lang
    except Exception as e:
        logging.warning(f"Langdetect failed: {e}, returning 'unknown'.")
        return "unknown"

def get_translation_pipeline(source_lang_code, target_lang_code):
    """Loads or retrieves a cached translation pipeline and tokenizer."""
    global TRANSLATION_PIPELINES, TOKENIZERS
    pipe_key = f"{source_lang_code}_to_{target_lang_code}"

    if pipe_key not in TRANSLATION_PIPELINES:
        logging.info(f"Translation pipeline cache miss for: {pipe_key}. Attempting to load.")
        retries = 3
        model = None
        tokenizer = None

        for attempt in range(retries):
            try:
                local_model_dir = os.path.join("models", "facebook", "nllb-200-distilled-600M")

                if os.path.isdir(local_model_dir):
                    model_name_or_path = local_model_dir
                    logging.info(f"Found local model directory: {model_name_or_path}")
                else:
                    model_name_or_path = "facebook/nllb-200-distilled-600M"
                    logging.info(f"Local model not found, using Hugging Face model: {model_name_or_path}")

                if model_name_or_path not in TOKENIZERS:
                     logging.info(f"Loading tokenizer for: {model_name_or_path}")
                     TOKENIZERS[model_name_or_path] = AutoTokenizer.from_pretrained(
                         model_name_or_path, src_lang=source_lang_code
                     )
                     logging.info("Tokenizer loaded and cached.")
                tokenizer = TOKENIZERS[model_name_or_path]

                logging.info(f"Loading model: {model_name_or_path}")
                model = AutoModelForSeq2SeqLM.from_pretrained(model_name_or_path)
                logging.info("Model loaded.")

                logging.info(f"Creating translation pipeline: {source_lang_code} -> {target_lang_code}")
                translator = pipeline(
                    'translation',
                    model=model,
                    tokenizer=tokenizer,
                    src_lang=source_lang_code,
                    tgt_lang=target_lang_code,
                    max_length=512
                )
                TRANSLATION_PIPELINES[pipe_key] = translator
                logging.info(f"Pipeline created and cached for {pipe_key}.")
                break

            except http.client.RemoteDisconnected as rd_err:
                logging.warning(f"RemoteDisconnected error (Attempt {attempt + 1}/{retries}): {rd_err}. Retrying in 2 seconds...")
                time.sleep(2)
                if attempt == retries - 1:
                     logging.error(f"Failed to load pipeline after {retries} attempts due to RemoteDisconnected.")
                     TRANSLATION_PIPELINES[pipe_key] = None

            except Exception as e:
                logging.error(f"Error loading translation pipeline {pipe_key} (Attempt {attempt + 1}): {e}")
                import traceback
                traceback.print_exc()
                TRANSLATION_PIPELINES[pipe_key] = None
                break

    return TRANSLATION_PIPELINES.get(pipe_key)


def translate_text(text, source_lang_short, target_lang_friendly_name):
    """
    Translates text using NLLB model.
    Args:
        text (str): Text to translate.
        source_lang_short (str): Short language code ('en', 'hi').
        target_lang_friendly_name (str): Friendly target language name ('Hindi', 'Tamil').
    Returns:
        tuple: (translated_text, error_message)
               translated_text is None if error occurs.
               error_message is None if successful.
    """
    if not text:
        return None, "No text provided for translation."

    nllb_source_code = NLLB_SOURCE_LANG_CODES.get(source_lang_short)
    if not nllb_source_code:
        return None, f"Source language short code '{source_lang_short}' not mapped to NLLB code."

    nllb_target_code = SUPPORTED_LANGUAGES.get(target_lang_friendly_name)
    if not nllb_target_code:
        return None, f"Target language name '{target_lang_friendly_name}' not mapped to NLLB code."

    logging.debug(f"Translation request: {nllb_source_code} -> {nllb_target_code}, Text: '{text[:50]}...'")

    try:
        translator = get_translation_pipeline(nllb_source_code, nllb_target_code)
        if translator is None:
            raise Exception(f"Translator pipeline for {nllb_source_code} -> {nllb_target_code} is not available.")

        logging.debug("Calling translator pipeline...")
        results = translator(text)
        if not results or not isinstance(results, list) or not results[0].get('translation_text'):
             logging.warning("Translator pipeline returned empty or invalid results:", results)
             raise Exception("Translation pipeline returned empty or invalid result format.")

        translated_text = results[0]['translation_text']
        logging.debug(f"Translation successful: '{translated_text[:100]}...'")
        return translated_text, None

    except Exception as e:
        logging.error(f"Error during translation ({nllb_source_code} -> {nllb_target_code}): {e}")
        return None, f"Translation failed: {e}"