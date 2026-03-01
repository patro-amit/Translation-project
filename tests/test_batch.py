import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import get_translation_pipeline
import time

pipe = get_translation_pipeline('eng_Latn', 'guj_Gujr')
print("Pipeline loaded.")

start = time.time()
res = pipe(["Hello world", "How are you?"])
print(res)
print(f"Time taken for 2 items: {time.time() - start:.2f} seconds")
