# app.py
from translator_override import translate_pipeline, check_model_availability
from translator_override import translate_pipeline
from simple_translator import translate_text, translate_pipeline, check_model_availability
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from werkzeug.utils import secure_filename
import os
import utils # Import our helper functions
from flask import jsonify
from models import db, TranslationLog
import sys
from gtts import gTTS
import io
from datetime import datetime
# Removed ZoneInfo imports as they were not requested for this fix.

# --- Configuration ---
UPLOAD_FOLDER = 'uploads'
INSTANCE_FOLDER = 'instance'
ALLOWED_EXTENSIONS_IMG = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}
ALLOWED_EXTENSIONS_AUDIO = {'mp3', 'wav', 'ogg', 'flac', 'm4a'}

app = Flask(__name__, instance_path=os.path.abspath(INSTANCE_FOLDER))

# API endpoint for model status (for frontend JS)
@app.route('/api/model-status')
def api_model_status():
    models = {}
    for lang_name, nllb_code in utils.SUPPORTED_LANGUAGES.items():
        try:
            available = check_model_availability(nllb_code)
        except Exception:
            available = False
        models[lang_name] = {"available": available}
    return jsonify({"success": True, "models": models})
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SECRET_KEY'] = 'your_very_secret_and_strong_key_here_12345' # CHANGE THIS!
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

for folder_name in [UPLOAD_FOLDER]:
    abs_folder_path = os.path.join(app.root_path, folder_name)
    if not os.path.exists(abs_folder_path):
        try:
            os.makedirs(abs_folder_path)
            # print(f"Created directory: {abs_folder_path}") # Less verbose for focused debug
        except OSError as e:
            print(f"ERROR: Could not create directory '{abs_folder_path}': {e}")
            sys.exit(1)
    if not os.access(abs_folder_path, os.W_OK):
        print(f"ERROR: Directory '{abs_folder_path}' is not writable.")

DATABASE_URI = f"sqlite:///{os.path.join(app.instance_path, 'translations.db')}"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
# print(f"Database URI: {DATABASE_URI}") # Less verbose

db.init_app(app)

with app.app_context():
    utils.initialize_models()
    db.create_all()

MASTER_TTS_CONFIG = {
    "asm_Beng": None, "ben_Beng": "bn", "guj_Gujr": "gu", "hin_Deva": "hi",
    "kan_Knda": "kn", "mal_Mlym": "ml", "mar_Deva": "mr", "ory_Orya": None,
    "pan_Guru": "pa", "tam_Taml": "ta", "tel_Telu": "te", "urd_Arab": "ur",
    "eng_Latn": "en",
}

NLLB_TO_FRIENDLY_NAME = {v: k for k, v in utils.SUPPORTED_LANGUAGES.items()}
NLLB_TO_FRIENDLY_NAME.update({v: k for k, v in utils.NLLB_SOURCE_LANG_CODES.items()})

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/api/languages')
def api_languages():
    langs = [
        {"code": k, "name": k}
        for k in utils.SUPPORTED_LANGUAGES.keys()
    ]
    return jsonify({"success": True, "languages": langs})

@app.route('/', methods=['GET', 'POST'])
def index_route():
    translation_result = None
    original_text = request.form.get('text_input', '') if request.method == 'POST' else ''
    detected_lang_nllb = "" # Will store NLLB code of detected source lang
    error = None

    default_target_friendly_name = list(utils.SUPPORTED_LANGUAGES.keys())[0]
    selected_target_friendly_name = request.form.get('target_language', default_target_friendly_name)

    main_result_tts_supported = False
    main_result_tts_code = 'en'

    if request.method == 'POST':
        # --- START OF FOCUSED DEBUGGING AREA ---
        print("\n--- POST Request Received ---")
        input_type = request.form.get('input_type')
        target_nllb_code = utils.SUPPORTED_LANGUAGES.get(selected_target_friendly_name)
        print(f"[DEBUG] Input Type: {input_type}, Target Lang (Friendly): {selected_target_friendly_name}, Target NLLB: {target_nllb_code}")

        log_entry = TranslationLog(target_language=target_nllb_code if target_nllb_code else "unknown_target")
        source_text_intermediate = None # Text extracted from OCR/STT/Input
        source_lang_detected_short = None # Short code like 'en', 'hi' from detection/Whisper
        # --- END OF FOCUSED DEBUGGING AREA ---

        try:
            if input_type == 'text':
                log_entry.input_type = 'text'
                source_text_intermediate = request.form.get('text_input', '').strip()
                original_text = source_text_intermediate
                if not source_text_intermediate:
                    raise ValueError("No text provided.")
                source_lang_detected_short = utils.detect_language(source_text_intermediate)
                if source_lang_detected_short not in utils.NLLB_SOURCE_LANG_CODES.keys():
                    flash(f"Detected language '{source_lang_detected_short}' for text input might not be directly translatable. Assuming 'English'.", "warning")
                    source_lang_detected_short = 'en'

            elif input_type in ['image', 'audio']:
                log_entry.input_type = 'ocr' if input_type == 'image' else 'audio'
                # --- START OF FOCUSED DEBUGGING AREA ---
                print(f"[DEBUG] File Input Type: {log_entry.input_type}")
                # --- END OF FOCUSED DEBUGGING AREA ---

                if 'file' not in request.files:
                    raise ValueError('No file part in request.')
                file = request.files['file']
                if file.filename == '':
                    raise ValueError('No file selected.')

                allowed_extensions = ALLOWED_EXTENSIONS_IMG if input_type == 'image' else ALLOWED_EXTENSIONS_AUDIO
                if file and allowed_file(file.filename, allowed_extensions):
                    filename = secure_filename(file.filename)
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    # --- START OF FOCUSED DEBUGGING AREA ---
                    print(f"[DEBUG] Saving uploaded file '{filename}' to: {filepath}")
                    # --- END OF FOCUSED DEBUGGING AREA ---
                    file.save(filepath)
                    # --- START OF FOCUSED DEBUGGING AREA ---
                    print(f"[DEBUG] File '{filename}' saved successfully.")
                    # --- END OF FOCUSED DEBUGGING AREA ---

                    try:
                        if input_type == 'image':
                            # --- START OF FOCUSED DEBUGGING AREA ---
                            print(f"[DEBUG] Performing OCR on {filepath}")
                            # --- END OF FOCUSED DEBUGGING AREA ---
                            source_text_intermediate, detected_lang_ocr_short = utils.perform_ocr(filepath)
                            # --- START OF FOCUSED DEBUGGING AREA ---
                            print(f"[DEBUG] OCR Result: Text='{str(source_text_intermediate)[:100]}...', Detected Lang='{detected_lang_ocr_short}'")
                            # --- END OF FOCUSED DEBUGGING AREA ---
                            source_lang_detected_short = detected_lang_ocr_short if detected_lang_ocr_short in utils.NLLB_SOURCE_LANG_CODES.keys() else 'en'
                        
                        elif input_type == 'audio':
                            print(f"[DEBUG] Performing STT on {filepath}")
                            # Let Whisper auto-detect language
                            stt_result_text, stt_detected_lang_short = utils.perform_stt(filepath)
                            source_text_intermediate = stt_result_text
                            # Map Whisper's detected language to supported codes (default to 'en' if not supported)
                            if stt_detected_lang_short in utils.NLLB_SOURCE_LANG_CODES:
                                source_lang_detected_short = stt_detected_lang_short
                            else:
                                flash(f"Detected language '{stt_detected_lang_short}' from audio is not supported for translation. Defaulting to English.", "warning")
                                source_lang_detected_short = 'en'
                            print(f"[DEBUG] STT Result: Text='{str(source_text_intermediate)[:100]}...', Detected Lang='{source_lang_detected_short}'")
                        
                        original_text = source_text_intermediate
                        if not source_text_intermediate:
                            # --- START OF FOCUSED DEBUGGING AREA ---
                            print(f"[DEBUG] ERROR: Text extraction failed for {log_entry.input_type}.")
                            # --- END OF FOCUSED DEBUGGING AREA ---
                            raise ValueError(f"Could not extract text using {log_entry.input_type}.")

                    except Exception as proc_err:
                        # --- START OF FOCUSED DEBUGGING AREA ---
                        print(f"[DEBUG] Error during file processing ({log_entry.input_type}): {proc_err}")
                        import traceback
                        traceback.print_exc() # Print full traceback for processing errors
                        # --- END OF FOCUSED DEBUGGING AREA ---
                        raise proc_err
                    finally:
                        if os.path.exists(filepath):
                            # --- START OF FOCUSED DEBUGGING AREA ---
                            print(f"[DEBUG] Removing temporary file: {filepath}")
                            # --- END OF FOCUSED DEBUGGING AREA ---
                            os.remove(filepath)
                else:
                    raise ValueError(f"File type '{file.filename.rsplit('.',1)[-1] if '.' in file.filename else 'unknown'}' not allowed or file error.")
            else:
                raise ValueError("Invalid input type specified.")

            # --- Perform Translation ---
            # --- START OF FOCUSED DEBUGGING AREA ---
            print(f"[DEBUG] Pre-Translation Check: source_text_intermediate is_not_None? {source_text_intermediate is not None}, source_lang_detected_short? '{source_lang_detected_short}', target_nllb_code? '{target_nllb_code}'")
            # --- END OF FOCUSED DEBUGGING AREA ---
            if source_text_intermediate and source_lang_detected_short and target_nllb_code:
                source_nllb_code = utils.NLLB_SOURCE_LANG_CODES.get(source_lang_detected_short)
                detected_lang_nllb = source_nllb_code

                if not source_nllb_code:
                    error_msg = f"Source language '{source_lang_detected_short}' (detected) could not be mapped to a supported translation model source code."
                    flash(error_msg, "danger")
                    error = error_msg
                    log_entry.error_message = error_msg
                else:
                    # --- START OF FOCUSED DEBUGGING AREA ---
                    print(f"[DEBUG] Calling utils.translate_text with: text='{source_text_intermediate[:50]}...', source_short='{source_lang_detected_short}', target_friendly='{selected_target_friendly_name}'")
                    # --- END OF FOCUSED DEBUGGING AREA ---
                    log_entry.source_language = source_nllb_code
                    log_entry.original_text = source_text_intermediate
                    translation_result, trans_error = utils.translate_text(
                        source_text_intermediate,
                        source_lang_detected_short,
                        selected_target_friendly_name
                    )
                    # --- START OF FOCUSED DEBUGGING AREA ---
                    print(f"[DEBUG] utils.translate_text returned: result='{str(translation_result)[:100]}...', error='{trans_error}'")
                    # --- END OF FOCUSED DEBUGGING AREA ---

                    if trans_error:
                        error = trans_error
                        log_entry.error_message = trans_error
                    elif translation_result:
                        log_entry.translated_text = translation_result
                        success = "Translation successful!"
                    else:
                        error = "Translation returned an empty result or failed silently."
                        log_entry.error_message = error
            else:
                 error_msg = "Missing critical information for translation (e.g., extracted text, source language, or target language not set after processing input)."
                 # --- START OF FOCUSED DEBUGGING AREA ---
                 print(f"[DEBUG] Skipping translation due to: {error_msg}")
                 # --- END OF FOCUSED DEBUGGING AREA ---
                 error = error_msg
                 log_entry.error_message = error_msg
                 pass

        except ValueError as ve:
            error = str(ve)
            log_entry.error_message = error
            print(f"[DEBUG] ValueError caught: {error}")
        except Exception as e:
            error = f"An unexpected error occurred: {e}"
            log_entry.error_message = error
            import traceback
            print("[DEBUG] --- UNEXPECTED EXCEPTION CAUGHT ---")
            traceback.print_exc()
            print("[DEBUG] ----------------------------------")

        try:
            if not log_entry.source_language: log_entry.source_language = "unknown_source"
            db.session.add(log_entry)
            db.session.commit()
        except Exception as db_err:
            db.session.rollback()
            print(f"Database Error during log commit: {db_err}") # This was already a good debug print
            pass
        # --- START OF FOCUSED DEBUGGING AREA ---
        print("--- POST Request Processing End ---")
        # --- END OF FOCUSED DEBUGGING AREA ---


    # Convert UTC timestamps to IST for display
    from datetime import timezone, timedelta
    import pytz
    IST = pytz.timezone('Asia/Kolkata')
    recent_logs = TranslationLog.query.order_by(TranslationLog.timestamp.desc()).limit(10).all()
    for log in recent_logs:
        if hasattr(log, 'timestamp') and log.timestamp:
            # Convert UTC to IST
            log.timestamp_ist = log.timestamp.replace(tzinfo=timezone.utc).astimezone(IST)
        else:
            log.timestamp_ist = None

    selected_nllb_for_main_result = utils.SUPPORTED_LANGUAGES.get(selected_target_friendly_name)
    if selected_nllb_for_main_result:
        tts_code_for_main = MASTER_TTS_CONFIG.get(selected_nllb_for_main_result)
        if tts_code_for_main:
            main_result_tts_supported = True
            main_result_tts_code = tts_code_for_main

    return render_template(
        'index.html',
        utils_supported_languages=utils.SUPPORTED_LANGUAGES,
        selected_target_lang=selected_target_friendly_name,
        original_text=original_text,
        translation_result=translation_result,
        detected_lang=NLLB_TO_FRIENDLY_NAME.get(detected_lang_nllb, detected_lang_nllb if detected_lang_nllb else "N/A"),
        error=error,
        success=locals().get('success', None),
        main_result_tts_supported=main_result_tts_supported,
        main_result_tts_code=main_result_tts_code,
        recent_logs=recent_logs,
        MASTER_TTS_CONFIG=MASTER_TTS_CONFIG,
        NLLB_TO_FRIENDLY_NAME=NLLB_TO_FRIENDLY_NAME,
        NLLB_TO_ISO=utils.NLLB_TO_ISO,
        current_year=datetime.now().year,
    )

@app.route('/tts', methods=['POST'])
def tts_route():
    text = request.form.get('text')
    tts_lang_code = request.form.get('lang', 'en')

    if not text: return "Missing text for TTS", 400
    if not tts_lang_code: return "Missing language code for TTS", 400

    # print(f"TTS Route Request: Text='{text[:50]}...', Lang='{tts_lang_code}'") # Already good
    try:
        gtts_instance = gTTS(text=text, lang=tts_lang_code, slow=False)
        fp = io.BytesIO()
        gtts_instance.write_to_fp(fp)
        fp.seek(0)
        # print(f"gTTS audio generated successfully for lang: {tts_lang_code}") # Already good
        return send_file(fp, mimetype='audio/mpeg')
    except Exception as e:
        print(f"gTTS generation failed for lang '{tts_lang_code}': {e}") # Already good
        import traceback
        traceback.print_exc() # Already good
        return f"TTS generation failed for gTTS with language '{tts_lang_code}': {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
