# AssemblyAI Transcript Downloader

## [Video Walkthrough](https://www.veed.io/view/a562623d-b689-4e5c-81b6-5e9f77cf31ad?panel=share)

This repository contains a Python application that takes a CSV file with a list of audio/video URLs as input and retrieves the transcript of each audio/video URL, saving them as text files in a folder named `transcripts_txt_files`. It accomplishes this task by utilizing the AssemblyAI Transcript API.

## Usage Instructions

Follow these steps to use this application:

1. **Clone the Repository:**

`git clone https://github.com/zkleb-aai/aai-csv-bulk-upload.git`


2. **Create a Python Virtual Environment:**

`python3 -m venv venv`


3. **Activate the Virtual Environment:**

On macOS/Linux: `source venv/bin/activate`

On Windows (Command Prompt): `venv\Scripts\activate`


4. **Install Requirements:**

`pip3 install -r requirements.txt`


5. **Create an Ngrok Connection:**
- Open a new terminal window.
- Start an Ngrok connection on port 5002:
  ```
  ngrok http 5002
  ```

6. **Create a `.env` File:**
- Create a file named `.env` in the project directory.
- Add your AssemblyAI API key to the `.env` file as follows:
  ```
  AAI_KEY=enter_your_assemblyai_api_key
  ```

7. **Start the Flask App:**
- Open another terminal window.
- Start the Flask application:
  ```
  python3 main.py
  ```

8. **Execute the Bulk Upload:**
- Put a CSV file containing the list of URLs for transcription in the project directory.
- Open another terminal window.
- Execute the bulk upload script:
  ```
  python3 bulk_upload.py
  ```
- You will be prompted to write the name of the CSV file.  Alternatively, you can also hardcode this CSV filename in [line 15 of the bulk_upload.py file](https://github.com/zkleb-aai/aai-csv-bulk-upload/blob/main/bulk_upload.py#L15).



9. **Check the Logs:**
- The Flask application logs will notify you of how many transcriptions have been received.
- You can monitor the progress and completion of the transcription process in these logs.

## Requirements

Make sure you have the following installed:
- Python 3.x
- Pip3 (Python package manager)
- [Ngrok](https://ngrok.com/) (for creating a public tunnel to your local Flask app)
