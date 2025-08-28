# extract_dictionary_from_flores.py
"""
Script to extract English-to-Indic word/phrase mappings from the FLORES-200 dataset.
This will help auto-populate your manual dictionaries for all supported languages.
"""
import os
import requests
import gzip

# FLORES-200 language codes for your supported languages
FLORES_CODES = {
    'hi': 'hin_Deva',
    'bn': 'ben_Beng',
    'gu': 'guj_Gujr',
    'as': 'asm_Beng',
    'kn': 'kan_Knda',
    'ml': 'mal_Mlym',
    'mr': 'mar_Deva',
    'or': 'ory_Orya',
    'pa': 'pan_Guru',
    'ta': 'tam_Taml',
    'te': 'tel_Telu',
    'ur': 'urd_Arab',
}

# Download URLs for FLORES-200 dev set (small, for demo)
BASE_URL = "https://raw.githubusercontent.com/facebookresearch/flores/main/flores200/dev/"
EN_FILE = BASE_URL + "dev.eng_Latn"  # English

os.makedirs("flores_data", exist_ok=True)

# Download English file
print("Downloading English dev set...")
r = requests.get(EN_FILE)
with open("flores_data/dev.eng_Latn", "w", encoding="utf-8") as f:
    f.write(r.text)

# Download and extract for each language
for lang, flores_code in FLORES_CODES.items():
    url = BASE_URL + f"dev.{flores_code}"
    print(f"Downloading {lang} dev set from {url} ...")
    r = requests.get(url)
    out_path = f"flores_data/dev.{flores_code}"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(r.text)

print("\nAll FLORES-200 dev files downloaded to ./flores_data/")

# Extract dictionary entries (first 100 lines for demo)
print("\nExtracting dictionary entries...")
with open("flores_data/dev.eng_Latn", encoding="utf-8") as f:
    en_lines = [line.strip() for line in f.readlines()]

for lang, flores_code in FLORES_CODES.items():
    with open(f"flores_data/dev.{flores_code}", encoding="utf-8") as f:
        tgt_lines = [line.strip() for line in f.readlines()]
    # Pair up and take first 100 for demo
    pairs = list(zip(en_lines, tgt_lines))[:100]
    dict_path = f"dictionaries/flores_en_{lang}.txt"
    with open(dict_path, "w", encoding="utf-8") as f:
        for en, tgt in pairs:
            f.write(f"{en}\t{tgt}\n")
    print(f"Saved: {dict_path}")

print("\nDictionary extraction complete. You can now use these files to expand your manual_dictionaries.py.")
