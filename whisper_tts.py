from pathlib import Path
from openai import OpenAI
from openai_client import openai_client

# OpenAI Client Setup
client = openai_client

# Open or create the file for reading the transcript 
with open("text.txt", encoding="utf8") as file:
    input_text = file.read()


speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input= input_text
)

response.stream_to_file(speech_file_path)