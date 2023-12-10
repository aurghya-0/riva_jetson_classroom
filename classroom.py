from openai_client import OpenAIKey
from openai import OpenAI
from audio_record import AudioRecord
from whisper_transcribe import Transcribe
from datetime import datetime

class Classroom:
    def __init__(self, class_name):
        self.client = OpenAI(api_key=OpenAIKey.key)
        self.DEBUG = False
        now = datetime.now()
        self.filename = now.strftime(f"%d-%m-%Y-%H-%M-%S - {class_name}")
    
    def record_class(self):
        r = AudioRecord(filename=f"{self.filename}.wav")
        r.record()

    def transcribe(self):
        t = Transcribe(self.client, f"{self.filename}.wav")
        t.create_transcript(filename=self.filename)

    def summarize(self):
        pass

    def create_class_notes(self):
        pass

    def debug(self):
        pass
