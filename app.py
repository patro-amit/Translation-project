# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, send_file, jsonify
from werkzeug.utils import secure_filename
import os
import utils # Import our helper functions
from models import db, TranslationLog
import sys
from gtts import gTTS
import io
from datetime import datetime
import secrets
import secrets
from schemes_data import get_schemes, get_scheme_by_id, get_daily_schemes

# --- Configuration ---
UPLOAD_FOLDER = 'uploads'
INSTANCE_FOLDER = 'instance'
ALLOWED_EXTENSIONS_IMG = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}
ALLOWED_EXTENSIONS_AUDIO = {'mp3', 'wav', 'ogg', 'flac', 'm4a'}

app = Flask(__name__, instance_path=os.path.abspath(INSTANCE_FOLDER))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or secrets.token_hex(32)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

for folder_name in [UPLOAD_FOLDER]:
    abs_folder_path = os.path.join(app.root_path, folder_name)
    if not os.path.exists(abs_folder_path):
        try:
            os.makedirs(abs_folder_path)
        except OSError as e:
            print(f"ERROR: Could not create directory '{abs_folder_path}': {e}")
            sys.exit(1)
    if not os.access(abs_folder_path, os.W_OK):
        print(f"ERROR: Directory '{abs_folder_path}' is not writable.")
        sys.exit(1)

DATABASE_URI = f"sqlite:///{os.path.join(app.instance_path, 'translations.db')}"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
# print(f"Database URI: {DATABASE_URI}") # Less verbose

db.init_app(app)

with app.app_context():
    utils.initialize_models()
    db.create_all()

# Disable caching for development
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

# Add cache-busting version to templates
import time
@app.context_processor
def inject_cache_buster():
    return {'cache_buster': int(time.time())}

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
        input_type = request.form.get('input_type')
        target_nllb_code = utils.SUPPORTED_LANGUAGES.get(selected_target_friendly_name)

        log_entry = TranslationLog()
        log_entry.target_language = target_nllb_code if target_nllb_code else "unknown_target"
        source_text_intermediate = None
        source_lang_detected_short = None

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

                if 'file' not in request.files:
                    raise ValueError('No file part in request.')
                file = request.files['file']
                if not file or not file.filename or file.filename == '':
                    raise ValueError('No file selected.')

                allowed_extensions = ALLOWED_EXTENSIONS_IMG if input_type == 'image' else ALLOWED_EXTENSIONS_AUDIO
                if file and file.filename and allowed_file(file.filename, allowed_extensions):
                    filename = secure_filename(file.filename)
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(filepath)

                    try:
                        if input_type == 'image':
                            source_text_intermediate, detected_lang_ocr_short = utils.perform_ocr(filepath)
                            source_lang_detected_short = detected_lang_ocr_short if detected_lang_ocr_short in utils.NLLB_SOURCE_LANG_CODES.keys() else 'en'
                        
                        elif input_type == 'audio':
                            stt_result_text, stt_detected_lang_short = utils.perform_stt(filepath, lang_code_hint='hi')
                            source_text_intermediate = stt_result_text
                            if stt_detected_lang_short in utils.NLLB_SOURCE_LANG_CODES:
                                source_lang_detected_short = stt_detected_lang_short
                            else:
                                flash(f"Detected language '{stt_detected_lang_short}' from audio is not supported for translation. Defaulting to English.", "warning")
                                source_lang_detected_short = 'en'
                        
                        original_text = source_text_intermediate
                        if not source_text_intermediate:
                            raise ValueError(f"Could not extract text using {log_entry.input_type}.")

                    except Exception as proc_err:
                        import traceback
                        traceback.print_exc()
                        raise proc_err
                    finally:
                        if os.path.exists(filepath):
                            os.remove(filepath)
                else:
                    file_ext = 'unknown'
                    if file.filename and '.' in file.filename:
                        file_ext = file.filename.rsplit('.', 1)[-1]
                    raise ValueError(f"File type '{file_ext}' not allowed or file error.")
            else:
                raise ValueError("Invalid input type specified.")

            # --- Perform Translation ---
            if source_text_intermediate and source_lang_detected_short and target_nllb_code:
                source_nllb_code = utils.NLLB_SOURCE_LANG_CODES.get(source_lang_detected_short)
                detected_lang_nllb = source_nllb_code

                if not source_nllb_code:
                    error_msg = f"Source language '{source_lang_detected_short}' (detected) could not be mapped to a supported translation model source code."
                    flash(error_msg, "danger")
                    error = error_msg
                    log_entry.error_message = error_msg
                else:
                    log_entry.source_language = source_nllb_code
                    log_entry.original_text = source_text_intermediate
                    translation_result, trans_error = utils.translate_text(
                        source_text_intermediate,
                        source_lang_detected_short,
                        selected_target_friendly_name
                    )

                    if trans_error:
                        error = trans_error
                        log_entry.error_message = trans_error
                        flash(f"Translation Error: {trans_error}", "danger")
                    elif translation_result:
                        log_entry.translated_text = translation_result
                        flash("Translation successful!", "success")
                    else:
                        error = "Translation returned an empty result or failed silently."
                        log_entry.error_message = error
                        flash(error, "warning")
            else:
                 error_msg = "Missing critical information for translation (e.g., extracted text, source language, or target language not set after processing input)."
                 error = error_msg
                 log_entry.error_message = error_msg
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

    recent_logs = TranslationLog.query.order_by(TranslationLog.timestamp.desc()).limit(10).all()
    # Removed ZoneInfo conversion for logs to keep focus on the primary issue

    selected_nllb_for_main_result = utils.SUPPORTED_LANGUAGES.get(selected_target_friendly_name)
    if selected_nllb_for_main_result:
        tts_code_for_main = MASTER_TTS_CONFIG.get(selected_nllb_for_main_result)
        if tts_code_for_main:
            main_result_tts_supported = True
            main_result_tts_code = tts_code_for_main

    detected_lang_display = "N/A"
    if detected_lang_nllb:
        detected_lang_display = NLLB_TO_FRIENDLY_NAME.get(detected_lang_nllb, detected_lang_nllb)
    
    return render_template(
        'index.html',
        utils_supported_languages=utils.SUPPORTED_LANGUAGES,
        selected_target_lang=selected_target_friendly_name,
        original_text=original_text,
        translation_result=translation_result,
        detected_lang=detected_lang_display,
        error=error,
        main_result_tts_supported=main_result_tts_supported,
        main_result_tts_code=main_result_tts_code,
        recent_logs=recent_logs,
        MASTER_TTS_CONFIG=MASTER_TTS_CONFIG,
        NLLB_TO_FRIENDLY_NAME=NLLB_TO_FRIENDLY_NAME,
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

# --- New API Routes for Enhanced Features ---

@app.route('/api/schemes/daily', methods=['GET'])
def get_daily_schemes_route():
    """Get schemes for daily display (rotates based on date)"""
    count = request.args.get('count', 3, type=int)
    schemes = get_daily_schemes(count)
    return jsonify({'schemes': schemes, 'success': True})

@app.route('/api/schemes/all', methods=['GET'])
def get_all_schemes_route():
    """Get all available government schemes"""
    limit = request.args.get('limit', 20, type=int)
    schemes = get_schemes(limit=limit)
    return jsonify({'schemes': schemes, 'success': True, 'count': len(schemes)})

@app.route('/api/schemes/<scheme_id>', methods=['GET'])
def get_scheme_detail_route(scheme_id):
    """Get detailed information about a specific scheme"""
    scheme = get_scheme_by_id(scheme_id)
    if scheme:
        return jsonify({'scheme': scheme, 'success': True})
    return jsonify({'success': False, 'error': 'Scheme not found'}), 404

@app.route('/api/schemes/all-with-translations', methods=['GET'])
def get_all_schemes_with_translations():
    """Get all schemes - returns English only, frontend handles caching and translation"""
    limit = request.args.get('limit', 20, type=int)
    schemes = get_schemes(limit=limit)
    
    # Return schemes in a format optimized for frontend caching
    schemes_data = []
    for scheme in schemes:
        schemes_data.append({
            'id': scheme['id'],
            'name': scheme['name'],
            'icon': scheme['icon'],
            'category': scheme['category'],
            'officialLink': scheme['officialLink'],
            'fullName': scheme['fullName'],
            'summary': scheme['summary']
        })
    
    return jsonify({
        'schemes': schemes_data,
        'success': True,
        'count': len(schemes_data)
    })

@app.route('/api/translate/instant', methods=['POST'])
def instant_translate_route():
    """Instant translation API for scheme text and other content"""
    data = request.get_json()
    text = data.get('text', '').strip()
    source_lang_short = data.get('source_lang', 'en')
    target_friendly_name = data.get('target_lang', 'Hindi')
    
    if not text:
        return jsonify({'success': False, 'error': 'No text provided'}), 400
    
    try:
        # Use existing translation function
        translation_result, trans_error = utils.translate_text(
            text,
            source_lang_short,
            target_friendly_name
        )
        
        if trans_error:
            return jsonify({'success': False, 'error': trans_error}), 500
        
        if translation_result:
            # Get TTS code for audio support
            target_nllb_code = utils.SUPPORTED_LANGUAGES.get(target_friendly_name)
            tts_code = MASTER_TTS_CONFIG.get(target_nllb_code) if target_nllb_code else None
            
            return jsonify({
                'success': True,
                'translated_text': translation_result,
                'source_lang': source_lang_short,
                'target_lang': target_friendly_name,
                'tts_supported': tts_code is not None,
                'tts_code': tts_code
            })
        else:
            return jsonify({'success': False, 'error': 'Translation returned empty result'}), 500
            
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/history/device', methods=['GET'])
def get_device_history_route():
    """Get translation history for a specific device"""
    device_id = request.args.get('device_id')
    limit = request.args.get('limit', 10, type=int)
    
    if not device_id:
        return jsonify({'success': False, 'error': 'Device ID required'}), 400
    
    try:
        # For now, return all recent logs
        # In a production app, you'd store device_id in TranslationLog model
        recent_logs = TranslationLog.query.order_by(
            TranslationLog.timestamp.desc()
        ).limit(limit).all()
        
        logs_data = []
        for log in recent_logs:
            logs_data.append({
                'id': log.id,
                'input_type': log.input_type,
                'source_language': log.source_language,
                'target_language': log.target_language,
                'original_text': log.original_text[:100] if log.original_text else '',
                'translated_text': log.translated_text[:100] if log.translated_text else '',
                'timestamp': log.timestamp.isoformat() if log.timestamp else None,
                'error_message': log.error_message
            })
        
        return jsonify({
            'success': True,
            'logs': logs_data,
            'count': len(logs_data),
            'device_id': device_id
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/translate/file', methods=['POST'])
def translate_file_instant_route():
    """Handle instant file translation (OCR/STT) without page reload"""
    try:
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'No file provided'}), 400
        
        file = request.files['file']
        input_type = request.form.get('input_type', 'image')
        target_friendly_name = request.form.get('target_language', 'Hindi')
        device_id = request.form.get('device_id', 'unknown')
        
        if not file or not file.filename:
            return jsonify({'success': False, 'error': 'No file selected'}), 400
        
        allowed_extensions = ALLOWED_EXTENSIONS_IMG if input_type == 'image' else ALLOWED_EXTENSIONS_AUDIO
        
        if not allowed_file(file.filename, allowed_extensions):
            return jsonify({'success': False, 'error': 'Invalid file type'}), 400
        
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            source_text = None
            source_lang_detected = 'en'
            
            if input_type == 'image':
                source_text, detected_lang = utils.perform_ocr(filepath)
                source_lang_detected = detected_lang if detected_lang in utils.NLLB_SOURCE_LANG_CODES.keys() else 'en'
            elif input_type == 'audio':
                source_text, detected_lang = utils.perform_stt(filepath, lang_code_hint='hi')
                source_lang_detected = detected_lang if detected_lang in utils.NLLB_SOURCE_LANG_CODES else 'en'
            
            if not source_text:
                return jsonify({'success': False, 'error': f'Could not extract text from {input_type}'}), 500
            
            # Translate the extracted text
            translation_result, trans_error = utils.translate_text(
                source_text,
                source_lang_detected,
                target_friendly_name
            )
            
            if trans_error:
                return jsonify({'success': False, 'error': trans_error}), 500
            
            # Log the translation
            log_entry = TranslationLog()
            log_entry.input_type = 'ocr' if input_type == 'image' else 'audio'
            log_entry.source_language = utils.NLLB_SOURCE_LANG_CODES.get(source_lang_detected)
            log_entry.target_language = utils.SUPPORTED_LANGUAGES.get(target_friendly_name)
            log_entry.original_text = source_text
            log_entry.translated_text = translation_result
            db.session.add(log_entry)
            db.session.commit()
            
            # Get TTS info
            target_nllb_code = utils.SUPPORTED_LANGUAGES.get(target_friendly_name)
            tts_code = MASTER_TTS_CONFIG.get(target_nllb_code) if target_nllb_code else None
            
            return jsonify({
                'success': True,
                'original_text': source_text,
                'translated_text': translation_result,
                'source_lang': source_lang_detected,
                'target_lang': target_friendly_name,
                'tts_supported': tts_code is not None,
                'tts_code': tts_code,
                'log_id': log_entry.id
            })
            
        finally:
            if os.path.exists(filepath):
                os.remove(filepath)
                
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)