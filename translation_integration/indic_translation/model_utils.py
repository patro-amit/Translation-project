# Modified model_utils.py for use with placeholder models
import os

# Define the supported languages and their model tags
LANGUAGE_CONFIGS = {
    'hi': {'name': 'Hindi', 'model_tag': 'hin_Deva'},
    'or': {'name': 'Oriya', 'model_tag': 'ory_Orya'},
    'bn': {'name': 'Bengali', 'model_tag': 'ben_Beng'},
    'ta': {'name': 'Tamil', 'model_tag': 'tam_Taml'},
    'te': {'name': 'Telugu', 'model_tag': 'tel_Telu'}
}

# Translation dictionary for demo purposes
SAMPLE_TRANSLATIONS = {
    'hi': {
        'hello': 'नमस्ते',
        'how are you': 'आप कैसे हैं',
        'good morning': 'शुभ प्रभात',
        'thank you': 'धन्यवाद',
        'welcome': 'स्वागत है'
    },
    'bn': {
        'hello': 'হ্যালো',
        'how are you': 'আপনি কেমন আছেন',
        'good morning': 'শুভ সকাল',
        'thank you': 'ধন্যবাদ',
        'welcome': 'স্বাগতম'
    },
    'or': {
        'hello': 'ନମସ୍କାର',
        'how are you': 'ଆପଣ କେମିତି ଅଛନ୍ତି',
        'good morning': 'ଶୁଭ ସକାଳ',
        'thank you': 'ଧନ୍ୟବାଦ',
        'welcome': 'ସ୍ୱାଗତ'
    },
    'ta': {
        'hello': 'வணக்கம்',
        'how are you': 'நீங்கள் எப்படி இருக்கிறீர்கள்',
        'good morning': 'காலை வணக்கம்',
        'thank you': 'நன்றி',
        'welcome': 'வரவேற்கிறோம்'
    },
    'te': {
        'hello': 'హలో',
        'how are you': 'మీరు ఎలా ఉన్నారు',
        'good morning': 'శుభోదయం',
        'thank you': 'ధన్యవాదాలు',
        'welcome': 'స్వాగతం'
    }
}

def get_supported_languages():
    """Get a list of supported languages with their codes and names"""
    return {code: config['name'] for code, config in LANGUAGE_CONFIGS.items()}

def translate_text(text, lang_code, model_dir="./models"):
    """
    Demo translate function - provides basic placeholder translations
    
    Args:
        text: English text to translate
        lang_code: Target language code
        model_dir: Directory containing the model files
    """
    if not text:
        return ""
    
    if lang_code not in LANGUAGE_CONFIGS:
        return f"Error: Unsupported language {lang_code}"
    
    # Check if the model files exist
    adapter_dir = os.path.join(model_dir, f"indictrans2-finetuned-en-to-{lang_code}-lora")
    adapter_config = os.path.join(adapter_dir, "adapter_config.json")
    adapter_model = os.path.join(adapter_dir, "adapter_model.bin")
    
    if not (os.path.exists(adapter_config) and os.path.exists(adapter_model)):
        return f"Model for {LANGUAGE_CONFIGS[lang_code]['name']} not found. Please ensure models are correctly installed."
    
    # Demo translation logic - check if text matches any sample phrases
    text_lower = text.lower()
    for key, translation in SAMPLE_TRANSLATIONS.get(lang_code, {}).items():
        if key in text_lower:
            return translation
    
    # For any other text, return a placeholder
    return f"[{LANGUAGE_CONFIGS[lang_code]['name']} translation of: {text}]"

def check_model_availability(model_dir="./models"):
    """Check which language models are available"""
    status = {}
    
    for code, config in LANGUAGE_CONFIGS.items():
        adapter_dir = os.path.join(model_dir, f"indictrans2-finetuned-en-to-{code}-lora")
        adapter_files_exist = (
            os.path.exists(adapter_dir) and
            os.path.exists(os.path.join(adapter_dir, "adapter_config.json")) and
            os.path.exists(os.path.join(adapter_dir, "adapter_model.bin"))
        )
        
        status[code] = {
            'name': config['name'],
            'available': adapter_files_exist
        }
    
    return status
