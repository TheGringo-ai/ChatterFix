import io
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

# Load credentials
def get_drive_service():
    creds = None
    for filename in os.listdir("."):
        if filename.endswith(".json") and "google-mpf" in filename:
            creds = service_account.Credentials.from_service_account_file(
                filename,
                scopes=["https://www.googleapis.com/auth/drive"]
            )
            break
    if not creds:
        raise FileNotFoundError("❌ No Google service account .json credentials found.")
    return build("drive", "v3", credentials=creds)

# List files
def list_files(limit=20):
    service = get_drive_service()
    results = service.files().list(
        pageSize=limit,
        fields="files(id, name, mimeType)"
    ).execute()
    return results.get("files", [])

# Download or export file depending on mimeType
def download_file(file_id, local_path):
    service = get_drive_service()

    file = service.files().get(fileId=file_id, fields="mimeType, name").execute()
    mime_type = file["mimeType"]

    if mime_type == "application/vnd.google-apps.document":
        request = service.files().export_media(fileId=file_id, mimeType="text/plain")
    elif mime_type == "application/vnd.google-apps.spreadsheet":
        request = service.files().export_media(fileId=file_id, mimeType="text/csv")
    else:
        request = service.files().get_media(fileId=file_id)

    fh = io.FileIO(local_path, "wb")
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while not done:
        status, done = downloader.next_chunk()
