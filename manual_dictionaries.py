# manual_dictionaries.py
"""
Automated multi-language manual dictionary for your translation project.
Add or update English-to-Target mappings for each language code.
"""

MANUAL_DICTIONARIES = {'as': {'404: Not Found': '404: Not Found'},
 'bn': {'404: Not Found': '404: Not Found',
        'Chrome': 'ক্রোম',
        'Kindle': 'কিন্ডল',
        'LLM': 'এলএলএম',
        'Natural Reader': 'ন্যাচারাল রিডার',
        'Plus': 'প্লাস',
        'Premium': 'প্রিমিয়াম',
        'YouTube': 'ইউটিউব',
        'app': 'অ্যাপ',
        'email': 'ইমেইল',
        'voice': 'ভয়েস'},
 'gu': {'404: Not Found': '404: Not Found'},
 'hi': {'404: Not Found': '404: Not Found',
        'Chrome': 'क्रोम',
        'Kindle': 'किंडल',
        'LLM': 'एलएलएम',
        'Natural Reader': 'नेचुरल रीडर',
        'Plus': 'प्लस',
        'Premium': 'प्रीमियम',
        'YouTube': 'यूट्यूब',
        'app': 'ऐप',
        'email': 'ईमेल',
        'voice': 'आवाज़'},
 'kn': {'404: Not Found': '404: Not Found'},
 'ml': {'404: Not Found': '404: Not Found'},
 'mr': {'404: Not Found': '404: Not Found'},
 'or': {'404: Not Found': '404: Not Found'},
 'pa': {'404: Not Found': '404: Not Found'},
 'ta': {'404: Not Found': '404: Not Found'},
 'te': {'404: Not Found': '404: Not Found'},
 'ur': {'404: Not Found': '404: Not Found'}}
def replace_with_manual_dictionary(text, lang_code):
    dictionary = MANUAL_DICTIONARIES.get(lang_code, {})
    for en, target in dictionary.items():
        text = text.replace(en, target)
    return text

# Example usage:
# text = replace_with_manual_dictionary(text, 'hi')
