import easyocr
import whisper
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer # Added AutoTokenizer
import os
from langdetect import detect
import time # Added for retry logic in get_translation_pipeline
import http.client # Added for retry logic in get_translation_pipeline

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
    print("[utils.py INFO] Initializing EasyOCR reader...")
    # Initialize EasyOCR with common languages to avoid reloading if possible
    # Adjust ['en', 'hi'] if you frequently OCR other specific scripts first
    OCR_READER = easyocr.Reader(['en', 'hi'], gpu=False)
    print("[utils.py INFO] EasyOCR reader initialized.")

    print("[utils.py INFO] Loading Whisper model (base)...")
    # Consider smaller ('tiny') or larger models based on performance/accuracy needs
    WHISPER_MODEL = whisper.load_model("base")
    print("[utils.py INFO] Whisper model loaded.")

# --- OCR Functions ---
# Note: Reloading EasyOCR reader per call can be slow. Consider caching readers.
# The current implementation reloads based on lang_code hint, which might not be optimal.
def get_easyocr_reader(lang_code):
    # This function is potentially inefficient if called repeatedly with different codes.
    # A better approach might be a shared reader or a cache.
    # For now, keeping original logic but adding print statement.
    supported_scripts = ['en', 'hi', 'mr', 'ne'] # Common Devanagari + English
    if lang_code in ['ta', 'te', 'kn', 'ml', 'bn', 'as', 'gu', 'pa', 'ur', 'or']:
        langs_to_load = [lang_code, 'en']
        print(f"[utils.py DEBUG] Initializing EasyOCR for specific script: {langs_to_load}")
        return easyocr.Reader(langs_to_load, gpu=False)
    else:
        # Default to English and Hindi/Marathi/Nepali (common Devanagari)
        print(f"[utils.py DEBUG] Initializing EasyOCR for default scripts: {supported_scripts}")
        return easyocr.Reader(supported_scripts, gpu=False)


def perform_ocr(image_path, lang_code='en'):
    # Note: Using a language hint might not be reliable. EasyOCR often works
    # better detecting languages automatically if multiple are loaded in the Reader.
    # Consider using the globally initialized OCR_READER if sufficient.
    print(f"[utils.py DEBUG] Performing OCR on: {image_path} (Hint: {lang_code})")
    # reader = get_easyocr_reader(lang_code) # Using the potentially inefficient per-call reader
    if OCR_READER is None:
         print("[utils.py ERROR] Global EasyOCR reader not initialized!")
         # Fallback to creating one - might be slow
         reader = easyocr.Reader(['en','hi'], gpu=False)
    else:
        # Using the global reader - likely more efficient if initialized correctly.
        # Ensure initialize_models() included the necessary languages.
        reader = OCR_READER

    try:
        # `paragraph=True` can sometimes group text better. `detail=0` gets only text.
        result = reader.readtext(image_path, detail=0, paragraph=True)
        text = " ".join(result)
        print(f"[utils.py DEBUG] OCR Raw Text: {text[:100]}...")
    except Exception as ocr_err:
        print(f"[utils.py ERROR] EasyOCR readtext failed: {ocr_err}")
        text = "" # Ensure text is empty on failure

    # Language detection on potentially mixed/short OCR text is unreliable
    detected_lang = 'en' # Defaulting to 'en' is safer
    if text:
        try:
            detected_lang = detect(text)
            print(f"[utils.py DEBUG] Langdetect on OCR text: {detected_lang}")
        except Exception as detect_err:
            print(f"[utils.py WARNING] Langdetect failed on OCR text: {detect_err}, defaulting to 'en'.")
            detected_lang = 'en'
    else:
        print("[utils.py WARNING] OCR produced no text, defaulting lang to 'en'.")

    # Return the short lang code ('en', 'hi', etc.)
    return text, detected_lang

# --- STT Function ---
def perform_stt(audio_path, lang_code_hint=None):
    # Added debugging prints and fp16=False flag
    global WHISPER_MODEL # Ensure we are using the globally loaded model
    if WHISPER_MODEL is None:
        print("[utils.py ERROR] Whisper model is None in perform_stt!")
        raise Exception("Whisper model not initialized.")
    try:
        print(f"[utils.py DEBUG] Starting Whisper transcription for: {audio_path}")
        # If a language hint is provided, use it; else let Whisper auto-detect
        if lang_code_hint:
            print(f"[utils.py DEBUG] Forcing Whisper language: {lang_code_hint}")
            result = WHISPER_MODEL.transcribe(audio_path, fp16=False, language=lang_code_hint)
        else:
            result = WHISPER_MODEL.transcribe(audio_path, fp16=False)
        text = result['text']
        lang_short = result['language']
        print(f"[utils.py DEBUG] Whisper transcription successful. Lang='{lang_short}', Text='{text[:100]}...'")
        return text, lang_short
    except Exception as e:
        print(f"[utils.py ERROR] Error during STT transcription: {e}")
        import traceback
        traceback.print_exc()
        return None, None
    
# --- Language Detection Function ---
def detect_language(text):
    if not text:
        return "unknown"
    try:
        lang = detect(text)
        print(f"[utils.py DEBUG] Langdetect on input text: {lang}")
        return lang
    except Exception as e:
        print(f"[utils.py WARNING] Langdetect failed: {e}, returning 'unknown'.")
        return "unknown"

# --- Translation Functions ---
def get_translation_pipeline(source_lang_code, target_lang_code):
    """Loads or retrieves a cached translation pipeline and tokenizer."""
    global TRANSLATION_PIPELINES, TOKENIZERS
    pipe_key = f"{source_lang_code}_to_{target_lang_code}"

    if pipe_key not in TRANSLATION_PIPELINES:
        print(f"[utils.py INFO] Translation pipeline cache miss for: {pipe_key}. Attempting to load.")
        retries = 3
        model = None # Initialize model variable
        tokenizer = None # Initialize tokenizer variable

        for attempt in range(retries):
            try:
                # Define potential local path more robustly
                # Assuming utils.py is in the root of the project, adjust path if needed
                # project_root = os.path.dirname(os.path.abspath(__file__))
                # local_model_dir = os.path.join(project_root, "models", "facebook", "nllb-200-distilled-600M")
                # Simplified path assumption (relative to where script is run, or needs adjustment)
                local_model_dir = os.path.join("models", "facebook", "nllb-200-distilled-600M")

                if os.path.isdir(local_model_dir):
                    model_name_or_path = local_model_dir
                    print(f"[utils.py INFO] Found local model directory: {model_name_or_path}")
                else:
                    model_name_or_path = "facebook/nllb-200-distilled-600M"
                    print(f"[utils.py INFO] Local model not found, using Hugging Face model: {model_name_or_path}")

                # Load tokenizer separately and cache it
                if model_name_or_path not in TOKENIZERS:
                     print(f"[utils.py INFO] Loading tokenizer for: {model_name_or_path}")
                     TOKENIZERS[model_name_or_path] = AutoTokenizer.from_pretrained(
                         model_name_or_path, src_lang=source_lang_code # Pass src_lang here
                     )
                     print(f"[utils.py INFO] Tokenizer loaded and cached.")
                tokenizer = TOKENIZERS[model_name_or_path]

                # Load model
                print(f"[utils.py INFO] Loading model: {model_name_or_path}")
                model = AutoModelForSeq2SeqLM.from_pretrained(model_name_or_path)
                print(f"[utils.py INFO] Model loaded.")

                # Create pipeline
                print(f"[utils.py INFO] Creating translation pipeline: {source_lang_code} -> {target_lang_code}")
                translator = pipeline(
                    'translation',
                    model=model, # Pass loaded model
                    tokenizer=tokenizer, # Pass loaded tokenizer
                    src_lang=source_lang_code,
                    tgt_lang=target_lang_code,
                    max_length=512 # Consider making this dynamic or removing if default is okay
                )
                TRANSLATION_PIPELINES[pipe_key] = translator
                print(f"[utils.py INFO] Pipeline created and cached for {pipe_key}.")
                break # Success, exit retry loop

            except http.client.RemoteDisconnected as rd_err:
                print(f"[utils.py WARNING] RemoteDisconnected error (Attempt {attempt + 1}/{retries}): {rd_err}. Retrying in 2 seconds...")
                time.sleep(2)
                if attempt == retries - 1:
                     print(f"[utils.py ERROR] Failed to load pipeline after {retries} attempts due to RemoteDisconnected.")
                     TRANSLATION_PIPELINES[pipe_key] = None # Mark as failed

            except Exception as e:
                print(f"[utils.py ERROR] Error loading translation pipeline {pipe_key} (Attempt {attempt + 1}): {e}")
                import traceback
                traceback.print_exc()
                TRANSLATION_PIPELINES[pipe_key] = None # Mark as failed
                break # Don't retry on other exceptions

    # Return the cached pipeline (or None if loading failed)
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

    # Map short source code ('en', 'hi') to NLLB source code
    nllb_source_code = NLLB_SOURCE_LANG_CODES.get(source_lang_short)
    if not nllb_source_code:
         # This check might be redundant if app.py already validates, but good defense
        return None, f"Source language short code '{source_lang_short}' not mapped to NLLB code."

    # Map friendly target name ('Hindi') to NLLB target code
    nllb_target_code = SUPPORTED_LANGUAGES.get(target_lang_friendly_name)
    if not nllb_target_code:
        return None, f"Target language name '{target_lang_friendly_name}' not mapped to NLLB code."

    print(f"[utils.py DEBUG] Translation request: {nllb_source_code} -> {nllb_target_code}, Text: '{text[:50]}...'")

    try:
        translator = get_translation_pipeline(nllb_source_code, nllb_target_code)
        if translator is None: # Check if loading failed
            # Error message should have been printed in get_translation_pipeline
            raise Exception(f"Translator pipeline for {nllb_source_code} -> {nllb_target_code} is not available.")

        # Perform the translation
        print(f"[utils.py DEBUG] Calling translator pipeline...")
        results = translator(text)
        # Ensure results are not empty and have the expected key
        if not results or not isinstance(results, list) or not results[0].get('translation_text'):
             print("[utils.py WARNING] Translator pipeline returned empty or invalid results:", results)
             raise Exception("Translation pipeline returned empty or invalid result format.")

        translated_text = results[0]['translation_text']
        print(f"[utils.py DEBUG] Translation successful: '{translated_text[:100]}...'")
        return translated_text, None # Success

    except Exception as e:
        print(f"[utils.py ERROR] Error during translation ({nllb_source_code} -> {nllb_target_code}): {e}")
        # Optionally print full traceback for debugging
        # import traceback
        # traceback.print_exc()
        # Return None for text, and the error message
        return None, f"Translation failed: {e}"