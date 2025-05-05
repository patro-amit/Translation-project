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

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/shyampatro/Translation Project/models/facebook/nllb-200-distilled-600M/service_account.json"

# --- Configuration ---
UPLOAD_FOLDER = 'uploads'
INSTANCE_FOLDER = 'instance'
ALLOWED_EXTENSIONS_IMG = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}
ALLOWED_EXTENSIONS_AUDIO = {'mp3', 'wav', 'ogg', 'flac', 'm4a'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max upload size
app.config['SECRET_KEY'] = '12345' # Change this!
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --- Ensure instance and upload folders exist and are writable ---
for folder in [UPLOAD_FOLDER, INSTANCE_FOLDER]:
    abs_folder = os.path.abspath(folder)
    if not os.path.exists(abs_folder):
        os.makedirs(abs_folder)
    if not os.access(abs_folder, os.W_OK):
        print(f"ERROR: Directory '{abs_folder}' is not writable.")
        sys.exit(1)
print(f"Instance folder absolute path: {os.path.abspath(INSTANCE_FOLDER)}")

# --- Use absolute path for SQLite DB ---
DATABASE_URI = f"sqlite:///{os.path.abspath(INSTANCE_FOLDER)}/translations.db"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

db.init_app(app)

# --- Initialize Models (Load once at startup) ---
with app.app_context():
    db.create_all()  # Create database tables if they don't exist

# --- Helper Functions ---
def allowed_file(filename, allowed_extensions):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

# --- Routes ---
@app.route('/', methods=['GET', 'POST'])
def index():
    translation_result = None
    original_text = ""
    detected_lang = ""
    error = None
    selected_target_lang = list(utils.SUPPORTED_LANGUAGES.keys())[0] # Default selection

    if request.method == 'POST':
        input_type = request.form.get('input_type')
        target_lang_name = request.form.get('target_language')
        selected_target_lang = target_lang_name # Keep selection after submit
        source_text = None
        source_lang = None
        log_entry = TranslationLog(target_language=utils.SUPPORTED_LANGUAGES.get(target_lang_name, 'unknown')) # Log NLLB code

        try:
            if input_type == 'text':
                log_entry.input_type = 'text'
                source_text = request.form.get('text_input', '').strip()
                if not source_text:
                    raise ValueError("No text provided.")
                # Attempt simple language detection
                source_lang = utils.detect_language(source_text)
                if source_lang not in ['en', 'hi']:
                    # Try defaulting or give error - NLLB needs explicit source
                    flash(f"Detected language '{source_lang}' might not be directly supported as source. Assuming 'en' or 'hi' might be needed.", "warning")
                    source_lang = 'en'

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
                            print(f"Performing OCR on {filepath}")
                            source_text, detected_lang_ocr = utils.perform_ocr(filepath)
                            source_lang = detected_lang_ocr if detected_lang_ocr in ['en', 'hi'] else 'en' # Assume EN if detection unclear
                        else: # audio
                            print(f"Performing STT on {filepath}")
                            source_text, detected_lang_stt = utils.perform_stt(filepath)
                            # Whisper often gives reliable lang codes ('en', 'hi')
                            source_lang = detected_lang_stt if detected_lang_stt in ['en', 'hi'] else 'en'

                        if not source_text:
                            raise ValueError(f"Could not extract text using {log_entry.input_type}.")

                    finally:
                        if os.path.exists(filepath):
                            os.remove(filepath) # Clean up uploaded file
                else:
                    raise ValueError('File type not allowed.')

            else:
                raise ValueError("Invalid input type specified.")

            # --- Perform Translation ---
            if source_text and source_lang and target_lang_name:
                print(f"Translating from {source_lang} to {target_lang_name}")
                log_entry.source_language = source_lang
                log_entry.original_text = source_text
                original_text = source_text # Display original text
                detected_lang = source_lang # Display detected source lang

                if source_lang not in utils.NLLB_SOURCE_LANG_CODES:
                    error_msg = f"Detected language '{source_lang}' is not supported for translation. Please enter text in English or Hindi."
                    flash(error_msg, "warning")
                    error = error_msg
                else:
                    translation_result, error = utils.translate_text(source_text, source_lang, target_lang_name)

                if error:
                    log_entry.error_message = error
                    flash(f"Translation Error: {error}", "danger")
                elif translation_result:
                    log_entry.translated_text = translation_result
                    flash("Translation successful!", "success")
                else:
                    log_entry.error_message = "Translation returned empty result."
                    flash("Translation failed or returned empty.", "warning")

            else:
                 error = "Missing source text, source language, or target language for translation."
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
            # Optionally log the full traceback for debugging
            import traceback
            traceback.print_exc()

        # --- Save log to DB ---
        try:
            # Only log if required fields are present
            if log_entry.source_language is None:
                log_entry.source_language = "unknown"
            if log_entry.target_language is None:
                log_entry.target_language = "unknown"
            # Only log if at least input_type and target_language are present
            if log_entry.input_type and log_entry.target_language:
                db.session.add(log_entry)
                db.session.commit()
        except Exception as db_err:
            db.session.rollback()
            print(f"Database Error: {db_err}")
            flash("Failed to log translation to database.", "secondary")

    # --- Prepare data for template ---
    # Get recent translations for display (optional)
    recent_logs = TranslationLog.query.order_by(TranslationLog.timestamp.desc()).limit(5).all()

    # --- Supported Indian languages for text-to-text translation (NLLB-200) ---
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
        # Add more as needed
    }
    # --- TTS support mapping (gTTS, Coqui, or not supported) ---
    TTS_LANG_CODES = {
        "Hindi": "hi",
        "Bengali": "bn",
        "Gujarati": "gu",
        "Kannada": "kn",
        "Malayalam": "ml",
        "Marathi": "mr",
        "Punjabi": "pa",
        "Tamil": "ta",
        "Telugu": "te",
        "Urdu": "ur",
        "English": "en",
        # Odia, Assamese, not supported by gTTS/Coqui/AWS/Google for free
    }
    TTS_SUPPORTED_LANGS = set(TTS_LANG_CODES.keys())
    # For unsupported TTS languages, create a set
    TTS_UNSUPPORTED_LANGS = set(SUPPORTED_LANGUAGES.keys()) - TTS_SUPPORTED_LANGS

    return render_template(
        'index.html',
        supported_languages=utils.SUPPORTED_LANGUAGES.keys(),
        selected_target_lang=selected_target_lang,
        original_text=original_text,
        detected_lang=detected_lang,
        translation_result=translation_result,
        error=error,
        recent_logs=recent_logs,
        utils=utils,
        tts_lang_codes=TTS_LANG_CODES,
        tts_supported_langs=TTS_SUPPORTED_LANGS,
        tts_unsupported_langs=TTS_UNSUPPORTED_LANGS,
        current_year=datetime.now().year,
    )

@app.route('/tts', methods=['POST'])
def tts():
    text = request.form.get('text')
    lang = request.form.get('lang', 'en')  # Should be 'hi' for Hindi
    tts = gTTS(text, lang=lang)
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return send_file(fp, mimetype='audio/mpeg')

if __name__ == '__main__':
    # Set debug=False for production
    app.run(debug=True, host='0.0.0.0', port=5001)