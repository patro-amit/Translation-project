import easyocr
import whisper
from transformers import pipeline
import os
from langdetect import detect

OCR_READER = None
WHISPER_MODEL = None
TRANSLATION_PIPELINES = {}

SUPPORTED_LANGUAGES = {
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
    "en": "eng_Latn",
    "hi": "hin_Deva"
}

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
    # Add more as needed
}

# Use all supported languages for OCR
reader = easyocr.Reader(['en', 'hi', 'bn', 'gu', 'kn', 'ml', 'mr', 'pa', 'ta', 'te', 'ur', 'as', 'or'])

def initialize_models():
    global OCR_READER, WHISPER_MODEL
    OCR_READER = easyocr.Reader(['en', 'hi'], gpu=False)
    WHISPER_MODEL = whisper.load_model("base")

def perform_ocr(image_path):
    result = reader.readtext(image_path, detail=0)
    text = " ".join(result)
    try:
        detected_lang = detect(text)
    except Exception:
        detected_lang = 'en'
    return text, detected_lang

def perform_stt(audio_path):
    if WHISPER_MODEL is None:
        raise Exception("Whisper model not initialized.")
    try:
        result = WHISPER_MODEL.transcribe(audio_path)
        text = result['text']
        lang = result['language']
        return text, lang
    except Exception as e:
        print(f"Error during STT: {e}")
        return None, None

def detect_language(text):
    try:
        return detect(text)
    except Exception:
        return "unknown"

def get_translation_pipeline(source_lang_code, target_lang_code):
    import time
    import http.client
    global TRANSLATION_PIPELINES
    pipe_key = f"{source_lang_code}_{target_lang_code}"
    if pipe_key not in TRANSLATION_PIPELINES:
        retries = 3
        for attempt in range(retries):
            try:
                local_model_dir = os.path.join(os.path.dirname(__file__), "models", "facebook", "nllb-200-distilled-600M")
                if os.path.isdir(local_model_dir):
                    model_name = local_model_dir
                else:
                    model_name = "facebook/nllb-200-distilled-600M"
                translator = pipeline(
                    'translation',
                    model=model_name,
                    src_lang=source_lang_code,
                    tgt_lang=target_lang_code,
                    max_length=512
                )
                TRANSLATION_PIPELINES[pipe_key] = translator
                break
            except http.client.RemoteDisconnected as e:
                print(f"RemoteDisconnected error: {e}. Retrying {attempt+1}/{retries}...")
                time.sleep(2)
            except Exception as e:
                print(f"Error loading translation pipeline {source_lang_code}->{target_lang_code}: {e}")
                TRANSLATION_PIPELINES[pipe_key] = None
                break
    return TRANSLATION_PIPELINES.get(pipe_key)

def translate_text(text, source_lang, target_lang_name):
    if not text:
        return None, "No text provided for translation."
    if source_lang not in NLLB_SOURCE_LANG_CODES:
        return None, f"Source language '{source_lang}' not supported for translation."
    if target_lang_name not in SUPPORTED_LANGUAGES:
        return None, f"Target language '{target_lang_name}' not supported."
    nllb_source_code = NLLB_SOURCE_LANG_CODES[source_lang]
    nllb_target_code = SUPPORTED_LANGUAGES[target_lang_name]
    try:
        translator = get_translation_pipeline(nllb_source_code, nllb_target_code)
        if not translator:
            raise Exception(f"Could not load/find translator for {nllb_source_code} -> {nllb_target_code}")
        results = translator(text)
        translated_text = results[0]['translation_text']
        return translated_text, None
    except Exception as e:
        print(f"Error during translation ({source_lang} -> {target_lang_name}): {e}")
        return None, f"Translation failed: {e}"


