# download_dictionaries.py
"""
Script to download and extract English-to-Indic dictionaries for supported languages in your project.
Uses AI4Bharat and IIT Bombay open datasets.
"""
import os
import requests
import zipfile

# Supported languages and their codes
LANGUAGES = {
    "Assamese": "as",
    "Bengali": "bn",
    "Gujarati": "gu",
    "Hindi": "hi",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Odia": "or",
    "Punjabi": "pa",
    "Tamil": "ta",
    "Telugu": "te",
    "Urdu": "ur",
}

# IIT Bombay dictionaries repo (small, word-level)
IITB_BASE_URL = "https://raw.githubusercontent.com/AI4Bharat/indicnlp_corpora/master/parallel/word-translations/"

# Output directory
os.makedirs("dictionaries", exist_ok=True)

for lang_name, lang_code in LANGUAGES.items():
    if lang_code == "en":
        continue
    url = f"{IITB_BASE_URL}en-{lang_code}.txt"
    out_path = f"dictionaries/en-{lang_code}.txt"
    print(f"Downloading {lang_name} dictionary from {url} ...")
    try:
        r = requests.get(url, timeout=30)
        if r.status_code == 200:
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(r.text)
            print(f"Saved: {out_path}")
        else:
            print(f"Not found: {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

print("\nAll available dictionaries downloaded to ./dictionaries/")
