
import os

# Define the supported languages and their model tags
LANGUAGE_CONFIGS = {
    'hi': {'name': 'Hindi', 'model_tag': 'hin_Deva'},
    'or': {'name': 'Oriya', 'model_tag': 'ory_Orya'},
    'bn': {'name': 'Bengali', 'model_tag': 'ben_Beng'},
    'ta': {'name': 'Tamil', 'model_tag': 'tam_Taml'},
    'te': {'name': 'Telugu', 'model_tag': 'tel_Telu'}
}

def get_supported_languages():
    """Get a list of supported languages with their codes and names"""
    return {code: config['name'] for code, config in LANGUAGE_CONFIGS.items()}

def translate_text(text, lang_code, model_dir="./models"):
    """
    Placeholder for translate function - in production this would use a trained model

    Args:
        text: English text to translate
        lang_code: Target language code
        model_dir: Directory containing the model files
    """
    if not text:
        return ""

    if lang_code not in LANGUAGE_CONFIGS:
        return f"Error: Unsupported language {lang_code}"

    # Just a demo translation
    return f"[This would be the {LANGUAGE_CONFIGS[lang_code]['name']} translation of: {text}]"
