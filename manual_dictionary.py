# manual_dictionary.py
"""
Template for a manual English-to-Indic dictionary for your translation project.
Fill in the words/phrases you want to always replace before translation.
"""

MANUAL_DICTIONARY = {
    # English : Hindi (add more as needed)
    "Chrome": "क्रोम",
    "app": "ऐप",
    "YouTube": "यूट्यूब",
    "Kindle": "किंडल",
    "email": "ईमेल",
    "voice": "आवाज़",
    "Natural Reader": "नेचुरल रीडर",
    "LLM": "एलएलएम",
    "Premium": "प्रीमियम",
    "Plus": "प्लस",
    # Add more technical/brand/common terms here
}

def replace_with_manual_dictionary(text, dictionary=MANUAL_DICTIONARY):
    for en, hi in dictionary.items():
        text = text.replace(en, hi)
    return text

# Example usage:
# text = replace_with_manual_dictionary(text)
