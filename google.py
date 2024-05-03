import os
import time
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.http import BatchHttpRequest


# Define your scopes and credentials file
SCOPES = ['https://www.googleapis.com/auth/drive']
CLIENT_SECRET_FILE = 'gdrive.json'  # Replace with your client secret file path
TOKEN_FILE = 'token.json'  # Replace with your token file path
FOLDER_ID = '1Qi2qUqobKOQ8kuRuZtGuqQDTySVDRgxg'  # Replace with the ID of the folder in which you want to upload the files

def get_credentials():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    return creds

def upload_file(service, file_path):
    file_name = os.path.basename(file_path)
    file_metadata = {
        'name': file_name,
        'parents': [FOLDER_ID]
    }

    media = MediaFileUpload(file_path, resumable=True)
    service.files().create(body=file_metadata, media_body=media, fields='id').execute()

def search_file_by_name(name):
    # Perform a query to search for the file by name
    response = service.files().list(q=f"name='{name}'").execute()
    files = response.get('files', [])

    if files:
        # Return the first file found
        return files[0]
    else:
        return None

def delete_file_by_name(name):
    # Search for the file by name
    file = search_file_by_name(name)
    if file:
        file_id = file['id']
        try:
            # Delete the file
            service.files().delete(fileId=file_id).execute()
            print(f"File '{name}' deleted successfully.")
        except Exception as e:
            print('An error occurred:', e)
    else:
        print(f"File '{name}' not found.")




credentials = get_credentials()
service = build('drive', 'v3', credentials=credentials)
file_name = 'logs.pdf'
delete_file_by_name(file_name)
for file_name in os.listdir('C:/Users/abel0/OneDrive/Desktop/Git/dropbox-ai-chat/dropboxfolder'):  
    if file_name.endswith('.pdf'):  # Upload only pdf files
        file_path = "dropboxfolder/"+file_name
        upload_file(service, file_path)
        print(f"{file_name} uploaded to Google Drive.")

