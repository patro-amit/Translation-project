# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from werkzeug.utils import secure_filename
import os
import utils # Import our helper functions
from models import db, TranslationLog
import sys
from gtts import gTTS
import io
from datetime import datetime
try:
    from zoneinfo import ZoneInfo  # Python 3.9+
except ImportError:
    from backports.zoneinfo import ZoneInfo  # For older Python, if installed
# import boto3 # Commented out if not immediately using Polly
# from botocore.exceptions import BotoCoreError, ClientError # Commented out
# from TTS.api import TTS # Commented out if not immediately using Coqui in /tts

# --- Configuration ---
UPLOAD_FOLDER = 'uploads'
INSTANCE_FOLDER = 'instance' # Relative path to instance folder
ALLOWED_EXTENSIONS_IMG = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}
ALLOWED_EXTENSIONS_AUDIO = {'mp3', 'wav', 'ogg', 'flac', 'm4a'}

app = Flask(__name__, instance_path=os.path.abspath(INSTANCE_FOLDER)) # Set instance_path
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max upload size
app.config['SECRET_KEY'] = 'your_very_secret_and_strong_key_here_12345' # CHANGE THIS!
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --- Ensure upload folder exists (Flask creates instance folder if instance_path is set) ---
for folder_name in [UPLOAD_FOLDER]: # Instance folder is handled by Flask if instance_path is set
    abs_folder_path = os.path.join(app.root_path, folder_name) # Use app.root_path for UPLOAD_FOLDER
    if not os.path.exists(abs_folder_path):
        try:
            os.makedirs(abs_folder_path)
            print(f"Created directory: {abs_folder_path}")
        except OSError as e:
            print(f"ERROR: Could not create directory '{abs_folder_path}': {e}")
            sys.exit(1)
    if not os.access(abs_folder_path, os.W_OK):
        print(f"ERROR: Directory '{abs_folder_path}' is not writable.")
        # sys.exit(1) # Be careful with sys.exit in production if permissions can be fixed

# --- Database Configuration ---
# Use instance_path for SQLite DB location
DATABASE_URI = f"sqlite:///{os.path.join(app.instance_path, 'translations.db')}"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
print(f"Database URI: {DATABASE_URI}")


db.init_app(app)

# --- Initialize AI Models (from utils.py) ---
# This should be called AFTER app context is available or handled within utils if models are global
with app.app_context():
    utils.initialize_models() # Ensure models are loaded (e.g., OCR, Whisper, Translation)
    db.create_all()  # Create database tables if they don't exist


# --- TTS Configuration ---
# MASTER_TTS_CONFIG maps NLLB language codes (from utils.SUPPORTED_LANGUAGES)
# to the language codes expected by your *primary* TTS engine (e.g., gTTS).
# Keys: NLLB codes (e.g., "hin_Deva"). Values: TTS engine codes (e.g., "hi" for gTTS).
MASTER_TTS_CONFIG = {
    # NLLB Code : gTTS Code (or other TTS engine code)
    "asm_Beng": None,       # Assamese (gTTS does not support 'as')
    "ben_Beng": "bn",       # Bengali
    "guj_Gujr": "gu",       # Gujarati
    "hin_Deva": "hi",       # Hindi
    "kan_Knda": "kn",       # Kannada
    "mal_Mlym": "ml",       # Malayalam
    "mar_Deva": "mr",       # Marathi
    "ory_Orya": None,       # Odia (gTTS does not support 'or')
    "pan_Guru": "pa",       # Punjabi (gTTS supports 'pa', but verify quality)
    "tam_Taml": "ta",       # Tamil
    "tel_Telu": "te",       # Telugu
    "urd_Arab": "ur",       # Urdu (gTTS supports 'ur', but verify quality)
    "eng_Latn": "en",       # English (assuming NLLB uses 'eng_Latn' for English source)
    # Add any other source/target NLLB codes from your utils.py that have TTS support
}

# --- Coqui TTS (Optional - keep if you plan to integrate it selectively) ---
# try:
#     coqui_tts_model = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=False)
#     # Print available speakers (for debugging/setup)
#     # print("Coqui TTS Speakers:", coqui_tts_model.speakers)
#     # Map your NLLB language codes to Coqui TTS language tags
#     COQUI_LANG_MAP_NLLB = {
#         'hin_Deva': 'hi', # Example, replace with actual Coqui language tag
#         # ... add other mappings from NLLB codes to Coqui language tags ...
#     }
#     # Example: pick a default speaker if needed for Coqui
#     # DEFAULT_COQUI_SPEAKER = coqui_tts_model.speakers[0] if coqui_tts_model.speakers else None
# except Exception as e:
#     print(f"Warning: Coqui TTS model could not be loaded: {e}")
#     coqui_tts_model = None


# --- Helper for NLLB to Friendly Name ---
# This creates a reverse map: NLLB Code -> Friendly Name
# e.g., {"hin_Deva": "Hindi", "tam_Taml": "Tamil"}
NLLB_TO_FRIENDLY_NAME = {v: k for k, v in utils.SUPPORTED_LANGUAGES.items()}
# Add source NLLB codes to this map as well, if they are different and might appear in logs
NLLB_TO_FRIENDLY_NAME.update({v: k for k, v in utils.NLLB_SOURCE_LANG_CODES.items()})


def allowed_file(filename, allowed_extensions):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions


# app.py
# ... (other imports and configurations) ...

@app.route('/', methods=['GET', 'POST'])
def index_route(): # Ensure the function name matches here
    translation_result = None
    original_text = request.form.get('text_input', '') if request.method == 'POST' else ''
    detected_lang_nllb = ""
    error = None

    default_target_friendly_name = list(utils.SUPPORTED_LANGUAGES.keys())[0]
    selected_target_friendly_name = request.form.get('target_language', default_target_friendly_name)

    # Initialize TTS support variables for main result
    main_result_tts_supported = False
    main_result_tts_code = 'en'

    if request.method == 'POST':
        input_type = request.form.get('input_type')
        target_nllb_code = utils.SUPPORTED_LANGUAGES.get(selected_target_friendly_name)

        log_entry = TranslationLog(target_language=target_nllb_code if target_nllb_code else "unknown_target")
        source_text_intermediate = None
        source_lang_detected_short = None

        try:
            if input_type == 'text':
                log_entry.input_type = 'text'
                source_text_intermediate = request.form.get('text_input', '').strip()
                original_text = source_text_intermediate # Update original_text for display
                if not source_text_intermediate:
                    raise ValueError("No text provided.")
                source_lang_detected_short = utils.detect_language(source_text_intermediate)
                if source_lang_detected_short not in utils.NLLB_SOURCE_LANG_CODES.keys(): # Check against keys of NLLB_SOURCE_LANG_CODES
                    flash(f"Detected language '{source_lang_detected_short}' might not be directly translatable. Assuming 'English'.", "warning")
                    source_lang_detected_short = 'en'

            elif input_type in ['image', 'audio']:
                if 'file' not in request.files:
                    raise ValueError('No file part in request.')
                file = request.files['file']
                if file.filename == '':
                    raise ValueError('No file selected.')

                allowed_extensions = ALLOWED_EXTENSIONS_IMG if input_type == 'image' else ALLOWED_EXTENSIONS_AUDIO
                log_entry.input_type = 'ocr' if input_type == 'image' else 'audio'

                if file and allowed_file(file.filename, allowed_extensions):
                    filename = secure_filename(file.filename)
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(filepath)

                    try:
                        if input_type == 'image':
                            source_text_intermediate, detected_lang_ocr_short = utils.perform_ocr(filepath)
                            source_lang_detected_short = detected_lang_ocr_short if detected_lang_ocr_short in utils.NLLB_SOURCE_LANG_CODES.keys() else 'en'
                        else: # audio
                            source_text_intermediate, detected_lang_stt_short = utils.perform_stt(filepath)
                            source_lang_detected_short = detected_lang_stt_short if detected_lang_stt_short in utils.NLLB_SOURCE_LANG_CODES.keys() else 'en'

                        if not source_text_intermediate:
                            raise ValueError(f"Could not extract text using {log_entry.input_type}.")
                        original_text = source_text_intermediate
                    finally:
                        if os.path.exists(filepath):
                            os.remove(filepath)
                else:
                    raise ValueError('File type not allowed or file error.')
            else:
                raise ValueError("Invalid input type specified.")

            if source_text_intermediate and source_lang_detected_short and target_nllb_code:
                source_nllb_code = utils.NLLB_SOURCE_LANG_CODES.get(source_lang_detected_short)
                detected_lang_nllb = source_nllb_code

                if not source_nllb_code:
                    error_msg = f"Source language '{source_lang_detected_short}' could not be mapped to a translation model code."
                    flash(error_msg, "danger")
                    error = error_msg
                    log_entry.error_message = error_msg
                else:
                    log_entry.source_language = source_nllb_code
                    log_entry.original_text = source_text_intermediate
                    translation_result, trans_error = utils.translate_text(source_text_intermediate, source_lang_detected_short, selected_target_friendly_name)

                    if trans_error:
                        error = trans_error
                        log_entry.error_message = trans_error
                        flash(f"Translation Error: {trans_error}", "danger")
                    elif translation_result:
                        log_entry.translated_text = translation_result
                        flash("Translation successful!", "success")
                    else:
                        error = "Translation returned an empty result."
                        log_entry.error_message = error
                        flash(error, "warning")
            else:
                 error = "Missing critical information for translation."
                 log_entry.error_message = error
                 flash(error, "danger")

        except ValueError as ve:
            error = str(ve)
            log_entry.error_message = error
            flash(f"Input Error: {error}", "warning")
        except Exception as e:
            error = f"An unexpected error occurred: {e}"
            log_entry.error_message = error
            flash(error, "danger")
            import traceback
            traceback.print_exc()

        try:
            if not log_entry.source_language: log_entry.source_language = "unknown_source"
            db.session.add(log_entry)
            db.session.commit()
        except Exception as db_err:
            db.session.rollback()
            print(f"Database Error during log commit: {db_err}")
            flash("Failed to save translation log to database.", "secondary")

    # This part runs for both GET and POST requests to prepare common template variables
    recent_logs = TranslationLog.query.order_by(TranslationLog.timestamp.desc()).limit(10).all()

    # Convert timestamps to IST for display
    IST = ZoneInfo('Asia/Kolkata')
    for log in recent_logs:
        if log.timestamp:
            log.timestamp_ist = log.timestamp.replace(tzinfo=ZoneInfo('UTC')).astimezone(IST)
        else:
            log.timestamp_ist = None

    selected_nllb_for_main_result = utils.SUPPORTED_LANGUAGES.get(selected_target_friendly_name)
    if selected_nllb_for_main_result: # Check if mapping exists
        tts_code_for_main = MASTER_TTS_CONFIG.get(selected_nllb_for_main_result) # Use .get() for safety
        if tts_code_for_main:
            main_result_tts_supported = True
            main_result_tts_code = tts_code_for_main

    # This is where 'utils_supported_languages' is defined for the template
    return render_template(
        'index.html',
        utils_supported_languages=utils.SUPPORTED_LANGUAGES, # <--- THIS IS THE KEY VARIABLE
        selected_target_lang=selected_target_friendly_name,
        original_text=original_text,
        translation_result=translation_result,
        detected_lang=NLLB_TO_FRIENDLY_NAME.get(detected_lang_nllb, detected_lang_nllb),
        error=error,
        main_result_tts_supported=main_result_tts_supported,
        main_result_tts_code=main_result_tts_code,
        recent_logs=recent_logs,
        MASTER_TTS_CONFIG=MASTER_TTS_CONFIG,
        NLLB_TO_FRIENDLY_NAME=NLLB_TO_FRIENDLY_NAME,
        current_year=datetime.now().year,
    )

# ... (rest of your app.py code, including tts_route) ...

@app.route('/tts', methods=['POST'])
def tts_route(): # Renamed to avoid conflict
    text = request.form.get('text')
    # 'lang' received here should be the TTS-engine specific code (e.g., "hi", "ta", "en")
    # This code comes directly from MASTER_TTS_CONFIG via the template
    tts_lang_code = request.form.get('lang', 'en')

    if not text:
        return "Missing text for TTS", 400
    if not tts_lang_code:
        return "Missing language code for TTS", 400

    print(f"TTS Request: Text='{text[:50]}...', Lang='{tts_lang_code}'")

    # --- Primarily use gTTS ---
    try:
        # gTTS directly uses short codes like 'hi', 'en', 'ta'
        gtts_instance = gTTS(text=text, lang=tts_lang_code, slow=False)
        fp = io.BytesIO()
        gtts_instance.write_to_fp(fp)
        fp.seek(0)
        print(f"gTTS audio generated successfully for lang: {tts_lang_code}")
        return send_file(fp, mimetype='audio/mpeg')
    except Exception as e:
        # This can happen if gTTS does not support the lang code or has other issues
        print(f"gTTS generation failed for lang '{tts_lang_code}': {e}")
        import traceback
        traceback.print_exc()
        # Fallback or specific error message
        # If you had Coqui or Polly integrated here, you could try them as fallbacks
        # For now, just return an error if gTTS fails
        return f"TTS generation failed with gTTS for language '{tts_lang_code}': {e}", 500


# Commenting out Polly route if not actively used to simplify
# @app.route('/polly', methods=['POST'])
# def polly_tts():
#     # ... your polly logic ...
#     pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)