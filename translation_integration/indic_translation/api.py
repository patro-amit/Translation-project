
from flask import Blueprint, request, jsonify
from .model_utils import get_supported_languages, translate_text
import os

# Create Blueprint
indic_translate_bp = Blueprint('indic_translate', __name__)

@indic_translate_bp.route('/api/languages', methods=['GET'])
def get_languages():
    """Return the list of supported languages"""
    languages = get_supported_languages()
    return jsonify({
        'success': True,
        'languages': [{'code': code, 'name': name} for code, name in languages.items()]
    })

@indic_translate_bp.route('/api/translate', methods=['POST'])
def translate():
    """Translate text from English to the target language"""
    # Parse request data
    data = request.json
    if not data:
        return jsonify({'success': False, 'error': 'No data provided'}), 400

    text = data.get('text', '').strip()
    if not text:
        return jsonify({'success': False, 'error': 'No text provided'}), 400

    target_lang = data.get('target_lang', '')
    if not target_lang:
        return jsonify({'success': False, 'error': 'No target language provided'}), 400

    # Placeholder for the model directory
    models_dir = os.environ.get('MODELS_DIR', './models')

    # Perform translation (demo only)
    translation = translate_text(text, target_lang, models_dir)

    return jsonify({
        'success': True,
        'translation': translation,
        'source_text': text,
        'target_lang': target_lang
    })

@indic_translate_bp.route('/api/model-status', methods=['GET'])
def model_status():
    """Check which models are available"""
    languages = get_supported_languages()

    # For demo purposes, pretend Oriya model is available
    status = {}
    for code, name in languages.items():
        status[code] = {
            'name': name,
            'available': code == 'or'  # Only Oriya is "available" in this demo
        }

    return jsonify({
        'success': True,
        'models': status
    })

# Function to register the Blueprint with a Flask app
def register_indic_translate_api(app):
    app.register_blueprint(indic_translate_bp)
