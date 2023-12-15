## TODO
# 1. Get PyDub to break down the audio file into 10 minute chunks
# 2. Get the transcript for each chunk
# 3. Write the transcript to a file

class Transcribe:
    def __init__(self, openai_client, input_file):
        self.client = openai_client
        self.audio_file = open(input_file, "rb")
        self.DEBUG = False

    def create_transcript(self, filename):
        self.transcript = self.client.audio.transcriptions.create(
            model="whisper-1",
            file=self.audio_file,
            response_format="text"
        )

        if self.DEBUG:
            self.debug()

        return self.transcript

    def debug(self):
        print(self.transcript)
