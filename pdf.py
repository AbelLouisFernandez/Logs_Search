import os
import time
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.http import BatchHttpRequest
import textwrap
import fpdf

def text_to_pdf(text,filename):
    file=open(text,'r')
    text=file.read()
    file.close()
    a4_width_mm = 210
    pt_to_mm = 0.35
    fontsize_pt = 10
    fontsize_mm = fontsize_pt * pt_to_mm
    margin_bottom_mm = 10
    character_width_mm = 7 * pt_to_mm
    width_text = a4_width_mm / character_width_mm

    pdf = fpdf.FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(True, margin=margin_bottom_mm)
    pdf.add_page()
    pdf.set_font(family='Courier', size=fontsize_pt)
    splitted = text.split('\n')

    for line in splitted:
        lines = textwrap.wrap(line, width_text)

        if len(lines) == 0:
            pdf.ln()

        for wrap in lines:
            pdf.cell(0, fontsize_mm, wrap, ln=1)

    pdf.output(filename, 'F')
SCOPES = ['https://www.googleapis.com/auth/drive']
CLIENT_SECRET_FILE = 'gdrive.json'  # Replace with your client secret file path
TOKEN_FILE = 'token.json'  # Replace with your token file path
FOLDER_ID = 'folder id of google drive'  # Replace with the ID of the folder in which you want to upload the files

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


def main():
    text_to_pdf("logs/logs.txt", "logs/logs.pdf")
    delete_file_by_name("logs.pdf")
    for file_name in os.listdir("location of folder where the logs of server is located"):  
        if file_name.endswith('.pdf'):  # Upload only pdf files
            file_path = "logs/"+file_name
            upload_file(service, file_path)
            print(f"{file_name} uploaded to Google Drive.")

if __name__ == "__main__":
    main()





