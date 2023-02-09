import requests
import datetime
from google.colauth import service_account
from googleapiclient.discovery import build

# URL of the file to download
file_url = "https://example.com/file.txt"

# Download the file
response = requests.get(file_url)
file_content = response.content

# Get today's date and check if it's the last day of the month
today = datetime.datetime.now().date()
if today.month != (today + datetime.timedelta(days=1)).month:
    # It's the last day of the month, save the file to Google Drive

    # Load the credentials for the service account
    credentials = service_account.Credentials.from_json_keyfile_name(
        "service_account.json",
        scopes=["https://www.googleapis.com/auth/drive"]
    )

    # Build the Drive API client
    drive_service = build("drive", "v3", credentials=credentials)

    # Define the metadata for the file
    file_metadata = {
        "name": "file.txt",
        "parents": ["<folder_id>"],
        "mimeType": "text/plain"
    }

    # Upload the file to Google Drive
    file = drive_service.files().create(body=file_metadata, media_body=file_content).execute()

    print(f"File saved to Google Drive with ID: {file['id']}")
else:
    print("Today is not the last day of the month.")
