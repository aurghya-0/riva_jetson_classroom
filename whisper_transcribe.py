from openai import OpenAI
from openai_client import openai_client

client = openai_client

## TODO
  # 1. Get PyDub to break down the audio file into 10 minute chunks
  # 2. Get the transcript for each chunk
  # 3. Write the transcript to a file

# get the recorded audio file
audio_file= open("output.wav", "rb")

# convert the audio file to transcript
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file,
  response_format="text"
)

# write the transcript as file
with open("transcript.txt", "w") as file:
    file.write(transcript)

# print the transcript
print(transcript)