# update_all_dictionaries.py
"""
Master script to fully automate dictionary enrichment for your translation project.
Runs all steps: download FLORES-200, extract pairs, and merge into manual_dictionaries.py.
"""
import subprocess
import sys

steps = [
    ("Downloading FLORES-200 and extracting pairs...", "python3 extract_dictionary_from_flores.py"),
    ("Merging extracted pairs into manual_dictionaries.py...", "python3 auto_merge_flores_to_manual_dict.py"),
]

for msg, cmd in steps:
    print(f"\n=== {msg} ===")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"Error running: {cmd}")
        sys.exit(1)

print("\nAll dictionaries updated and merged successfully!")
