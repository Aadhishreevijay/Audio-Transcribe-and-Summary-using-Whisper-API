import requests
import os
import whisper
import ssl


def downloadFile(url, save_path="C:\\Users\\shree\\OneDrive\\Desktop\\speech-2-text\\end\\media\\audio.mp3"):
    try:
        # It's recommended to verify SSL certificates
        ssl._create_default_https_context = ssl._create_unverified_context
        r = requests.get(url, allow_redirects=True)
        r.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        with open(save_path, "wb") as f:
            f.write(r.content)
        print(f"File downloaded successfully and saved to {save_path}")

    except requests.RequestException as e:
        print(f"An error occurred while downloading the file: {e}")


import os
import whisper
import traceback

def transcribe(audio_path="C:\\Users\\shree\\OneDrive\\Desktop\\speech-2-text\\end\\media\\audio.mp3"):
    try:
        # Print the path to ensure it’s correct
        print(f"Attempting to transcribe file at: {audio_path}")

        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"File not found at path: {audio_path}")

        # Initialize the Whisper ASR model
        model = whisper.load_model("base")

        # Transcribe the audio
        result = model.transcribe(audio_path)

        # Extract and return the transcript text
        return result["text"]

    except Exception as e:
        print(f"An error occurred during transcription: {e}")
        print(traceback.format_exc())
