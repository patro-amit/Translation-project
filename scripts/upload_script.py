import os
import sys
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_to_drive():
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    SERVICE_ACCOUNT_FILE = '/Users/shyampatro/Translation-project/models/facebook/nllb-200-distilled-600M/service_account.json'
    FILE_PATH = '/Users/shyampatro/Translation-project/models/facebook/nllb-200-distilled-600M/pytorch_model.bin'
    
    if not os.path.exists(SERVICE_ACCOUNT_FILE) or not os.path.exists(FILE_PATH):
        print("Missing credentials or model file!")
        sys.exit(1)

    print("Authenticating...")
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=creds)

    print("Uploading file (this may take a while for 2.4GB)...")
    file_metadata = {'name': 'pytorch_model.bin'}
    # resumable=True for large files over 5MB
    media = MediaFileUpload(FILE_PATH, mimetype='application/octet-stream', resumable=True)
    
    # Can configure chunk size. But default is fine, might be slightly slower. 
    # Use chunksize 100MB
    media = MediaFileUpload(FILE_PATH, mimetype='application/octet-stream', resumable=True, chunksize=100*1024*1024)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    file_id = file.get('id')
    print(f"File uploaded successfully! File ID: {file_id}")

    print("Setting permissions to public (anyone with link can read)...")
    permission = {
        'type': 'anyone',
        'role': 'reader',
    }
    service.permissions().create(fileId=file_id, body=permission).execute()
    print("Permissions updated.")
    
    with open('/Volumes/Sandisk/Translation-project/drive_model_id.txt', 'w') as f:
        f.write(file_id)

if __name__ == '__main__':
    upload_to_drive()
