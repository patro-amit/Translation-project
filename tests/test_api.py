import requests
import time

url = "http://127.0.0.1:5001/api/translate/batch"
data = {
    "texts": ["Welcome to India", "How are you today?"],
    "source_lang": "en",
    "target_lang": "Gujarati"
}

print("Testing Batch API...")
start = time.time()
try:
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
print(f"Time taken: {time.time() - start:.2f} seconds")
