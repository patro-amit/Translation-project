# auto_merge_flores_to_manual_dict.py
"""
Script to auto-merge extracted FLORES-200 dictionaries into your manual_dictionaries.py.
This will add new entries without overwriting your existing custom mappings.
"""
import os
import ast

MANUAL_DICT_PATH = "manual_dictionaries.py"
FLORES_DICT_DIR = "dictionaries"

# Load existing manual dictionaries
with open(MANUAL_DICT_PATH, encoding="utf-8") as f:
    code = f.read()
# Extract the MANUAL_DICTIONARIES dict from the file
start = code.find('MANUAL_DICTIONARIES =')
end = code.find('def replace_with_manual_dictionary')
manual_dict_code = code[start:end].strip()
manual_dict = ast.literal_eval(manual_dict_code.split('=',1)[1].strip())

# Map FLORES file suffix to language code
FLORES_LANGS = {
    'hi': 'hi', 'bn': 'bn', 'gu': 'gu', 'as': 'as', 'kn': 'kn', 'ml': 'ml',
    'mr': 'mr', 'or': 'or', 'pa': 'pa', 'ta': 'ta', 'te': 'te', 'ur': 'ur',
}

for lang in FLORES_LANGS:
    dict_file = os.path.join(FLORES_DICT_DIR, f"flores_en_{lang}.txt")
    if not os.path.exists(dict_file):
        continue
    with open(dict_file, encoding="utf-8") as f:
        for line in f:
            en, tgt = line.strip().split('\t')
            if not en or not tgt:
                continue
            # Only add if not already present
            if lang not in manual_dict:
                manual_dict[lang] = {}
            if en not in manual_dict[lang]:
                manual_dict[lang][en] = tgt

# Write back to manual_dictionaries.py
with open(MANUAL_DICT_PATH, encoding="utf-8") as f:
    lines = f.readlines()

# Find where MANUAL_DICTIONARIES starts and ends
start_idx = next(i for i,l in enumerate(lines) if l.strip().startswith('MANUAL_DICTIONARIES ='))
end_idx = next(i for i,l in enumerate(lines) if l.strip().startswith('def replace_with_manual_dictionary'))

# Replace the dictionary block
import pprint
new_dict_str = pprint.pformat(manual_dict, width=120, compact=False)
lines[start_idx] = f"MANUAL_DICTIONARIES = {new_dict_str}\n"
# Remove old lines in between
for i in range(start_idx+1, end_idx):
    lines[i] = ''

with open(MANUAL_DICT_PATH, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Manual dictionaries updated with FLORES-200 entries!")
