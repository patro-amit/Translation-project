# utils.py
import easyocr
# If "import whisper" is not resolved, you likely don't have the 'whisper' package installed.
# Install it using: pip install -U openai-whisper
# If you use a virtual environment, make sure it's activated.
import whisper
from transformers import pipeline
import os
from langdetect import detect # Optional

# --- Configuration ---
# Make sure models are downloaded (this might happen on first run)
# Consider loading models globally in app.py for efficiency instead of here
OCR_READER = None
WHISPER_MODEL = None
TRANSLATION_PIPELINES = {} # Cache pipelines

# --- Supported Languages ---
# Map user-friendly names to model codes (adjust based on chosen model)
# Example using NLLB codes (replace with actual codes for your target languages)
SUPPORTED_LANGUAGES = {
    "Assamese": "asm_Beng",
    "Bengali": "ben_Beng",
    "Gujarati": "guj_Gujr",
    "Hindi": "hin_Deva", # Source/Target
    "Kannada": "kan_Knda",
    "Malayalam": "mal_Mlym",
    "Marathi": "mar_Deva",
    "Odia": "ory_Orya",
    "Punjabi": "pan_Guru",
    "Tamil": "tam_Taml",
    "Telugu": "tel_Telu",
    "Urdu": "urd_Arab",
    # Add more as needed by your model
}
# NLLB Source Language Codes (for English/Hindi)
NLLB_SOURCE_LANG_CODES = {
    "en": "eng_Latn",
    "hi": "hin_Deva"
}


def initialize_models():
    """Loads models into memory. Call this once at app startup."""
    global OCR_READER, WHISPER_MODEL
    print("Initializing models...")
    # --- EasyOCR ---
    # Specify languages needed, e.g., English and Hindi
    OCR_READER = easyocr.Reader(['en', 'hi'], gpu=False) # Set gpu=True if available/configured
    print("EasyOCR Reader initialized.")

    # --- Whisper ---
    # Choose model size: 'tiny', 'base', 'small', 'medium', 'large'
    # Smaller models are faster but less accurate. 'base' or 'small' might be a good start.
    WHISPER_MODEL = whisper.load_model("base")
    print("Whisper model loaded.")
    # Translation pipelines will be loaded on demand in translate_text

    print("Models initialized.")


def perform_ocr(image_path):
    """Performs OCR on an image file."""
    if not OCR_READER:
        raise Exception("OCR Reader not initialized.")
    try:
        result = OCR_READER.readtext(image_path, detail=0, paragraph=True)
        text = " ".join(result)
        # Basic language detection (optional)
        lang = detect_language(text)
        return text, lang
    except Exception as e:
        print(f"Error during OCR: {e}")
        return None, None

def perform_stt(audio_path):
    """Performs Speech-to-Text on an audio file."""
    if not WHISPER_MODEL:
        raise Exception("Whisper model not initialized.")
    try:
        # Whisper can detect language automatically
        result = WHISPER_MODEL.transcribe(audio_path)
        text = result['text']
        lang = result['language'] # Whisper provides detected language
        return text, lang
    except Exception as e:
        print(f"Error during STT: {e}")
        return None, None

def detect_language(text):
    """Detects language using langdetect."""
    try:
        # Be cautious: langdetect might be unreliable for short/mixed text
        return detect(text)
    except:
        return "unknown" # Handle detection errors


def get_translation_pipeline(source_lang_code, target_lang_code):
    """Loads or retrieves a cached translation pipeline with retry logic for network errors."""
    import time
    import http.client
    global TRANSLATION_PIPELINES
    pipe_key = f"{source_lang_code}_{target_lang_code}"

    if pipe_key not in TRANSLATION_PIPELINES:
        retries = 3
        for attempt in range(retries):
            try:
                # Prefer local model directory if available
                local_model_dir = os.path.join(os.path.dirname(__file__), "models", "facebook", "nllb-200-distilled-600M")
                if os.path.isdir(local_model_dir):
                    model_name = local_model_dir
                    print(f"Using local model directory: {model_name}")
                else:
                    model_name = "facebook/nllb-200-distilled-600M"
                    print(f"Using Hugging Face Hub model: {model_name}")
                print(f"Loading translation pipeline: {model_name} for {source_lang_code} -> {target_lang_code}")
                translator = pipeline(
                    'translation',
                    model=model_name,
                    src_lang=source_lang_code,
                    tgt_lang=target_lang_code,
                    max_length=512
                )
                TRANSLATION_PIPELINES[pipe_key] = translator
                print("Pipeline loaded.")
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
    """Translates text using Hugging Face Transformers."""
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

        # Perform translation
        # NLLB models expect specific language codes to be set in the pipeline creation
        # The actual call might just need the text
        results = translator(text)
        translated_text = results[0]['translation_text']
        return translated_text, None # Return translated text, no error
    except Exception as e:
        print(f"Error during translation ({source_lang} -> {target_lang_name}): {e}")
        return None, f"Translation failed: {e}"


