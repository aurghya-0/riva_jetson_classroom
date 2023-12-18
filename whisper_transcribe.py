from custom_logger import getLogger
## TODO
# 1. Get PyDub to break down the audio file into 10 minute chunks
# 2. Get the transcript for each chunk
# 3. Write the transcript to a file

class Transcribe:
    """
    Transcribes the audio file using OpenAI API
    """
    def __init__(self, openai_client, input_file, DEBUG=False):
        """Class constructor

        Args:
            openai_client: openai client instance
            input_file (str): audio file to extract the transcription from
        """
        self.client = openai_client
        self.audio_file = open(input_file, "rb")

        if DEBUG:
            self.DEBUG = True
            self.log = getLogger()
        else:
            self.DEBUG = False

    def create_transcript(self):
        """Create transcript using the OpenAI API

        Args:
            filename (str): filename of the audio file

        Returns:
            str: transcript
        """
        self.log.info("> Creating transcript....")
        transcript = self.client.audio.transcriptions.create(
            model="whisper-1",
            file=self.audio_file,
            response_format="text"
        )

        if self.DEBUG:
            self.log.debug(f"TRANSCRIPT:\n{transcript}")
        
        self.log.info("> Transcript created....")
        return transcript
