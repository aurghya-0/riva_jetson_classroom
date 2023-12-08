from openai import OpenAI

# OpenAI Client Setup
client = OpenAI(
    api_key="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",
)

# get the recorded audio file
audio_file= open("output.wav", "rb")

# convert the audio file to transcript
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file,
  response_format="text"
)

with open("transcript.txt", "w") as file:
    file.write(transcript)

# print the transcript
print(transcript)