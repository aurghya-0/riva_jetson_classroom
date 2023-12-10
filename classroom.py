from openai_client import OpenAIKey
from openai import OpenAI
from audio_record import AudioRecord
from whisper_transcribe import Transcribe
from datetime import datetime
from class_notes import ClassNote

## TODO
# - Add a debug mode
# - Add a way to get the class duration from the user
# - Add a way to get the class name from the user
# - Organize the files into folders

class Classroom:
    def __init__(self, class_name, class_duration=10):
        self.client = OpenAI(api_key=OpenAIKey.key)
        self.DEBUG = False
        now = datetime.now()
        self.filename = now.strftime(f"%d-%m-%Y-%H-%M-%S - {class_name}")
        self.class_duration = class_duration
    
    def record_class(self):
        r = AudioRecord(
            filename=f"{self.filename}.wav", 
            seconds=self.class_duration)
        r.record()

    def transcribe(self):
        t = Transcribe(self.client, f"{self.filename}.wav")
        t.create_transcript(filename=self.filename)

    def summarize(self):
        self.cn = ClassNote(self.client, self.filename)
        self.cn.summarize()

    def create_class_notes(self):
        self.cn.create_notes_collection()

    def debug(self):
        pass
