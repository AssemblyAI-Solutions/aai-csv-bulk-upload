from flask import Flask, request, jsonify
import dotenv
import os
import requests
from helpers import db_functions

dotenv.load_dotenv()
aai_key=os.getenv("AAI_KEY")

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    id = request.args.get('id')
    data = request.json
    if data:
        transcript_id = data['transcript_id']
        polling_endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"
        headers = {
            "authorization": aai_key
        }

        transcription_result = requests.get(polling_endpoint, headers=headers).json()

        if transcription_result['status'] == 'completed':
            folder_path = 'transcripts_txt_files'
            file_name = transcription_result['audio_url'].split("?")[0].replace('https://','').replace('/','_') + '.txt'
            file_path = f'{folder_path}/{file_name}'
            try:
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # Open the file in write mode ('w')
                with open(file_path, 'w') as file:
                    # Write the data to the file
                    file.write(transcription_result['text'])
                db_functions.update_received_status(id)
                print(f"File '{file_name}' has been successfully written to '{folder_path}'.")
            except FileNotFoundError:
                print(f"Error: The folder '{folder_path}' does not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")
            print(db_functions.get_status())
        
        response_message = {"message": "Webhook received successfully"}
        return jsonify(response_message), 200
    else:
        return jsonify({"error": "Invalid webhook data"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
