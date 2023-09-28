import os
import dotenv
import requests
from helpers.get_ngrok_url import get_ngrok_url
import csv
from helpers.get_id import get_id
from helpers import db_functions

db_functions.createDb()

dotenv.load_dotenv()
aai_key=os.getenv("AAI_KEY")

def bulk_upload():
    csv_file_path = ''  # Replace with the path to your CSV file

    if not csv_file_path:
        csv_file_path = input('Please enter the file name of your CSV file: ')
    if not csv_file_path or not os.path.exists(csv_file_path):
        print("CSV file not found.")
        return None
        
    transcript_urls = []

    with open(csv_file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            for column in row:
                if column.strip():
                    transcript_urls.append(column.strip())

    base_url = "https://api.assemblyai.com/v2"
    url = base_url + "/transcript"
    headers = {"authorization": aai_key}
    ngrok_url = get_ngrok_url()

    counter = 0
    for audio_url in transcript_urls:
        id = get_id(audio_url)
        db_functions.addEntry(id,audio_url)
        data = {
            "webhook_url": ngrok_url+'/webhook?id='+id,
            "audio_url": audio_url
            }
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            counter += 1
            print(f"{audio_url} sent for transcription. URLs Sent = {counter}")
        else:
            print(f"{audio_url} failed to be sent for transcription. Response Code = {response.status_code}")

    return None

bulk_upload()