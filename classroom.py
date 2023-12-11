from openai_client import OpenAIKey
from openai import OpenAI
from audio_record import AudioRecord
from whisper_transcribe import Transcribe
from datetime import datetime
from class_notes import ClassNote
import os


# - Add a debug mode
# - Add a way to get the class duration from the user
# - Add a way to get the class name from the user
# - Organize the files into folders
# - Move everything to a database based system

class Classroom:
    def __init__(self, class_name, class_duration=10, subject="HPC"):
        self.client = OpenAI(api_key=OpenAIKey.key)
        self.DEBUG = False
        now = datetime.now()
        self.filename = now.strftime(f"%d-%m-%Y-%H-%M-%S - {class_name}")
        self.class_duration = class_duration
        self.subject = subject
        self.date = datetime.now().strftime("%d-/%m-/%Y")

        self.output_path = f"{self.subject}/{self.date}"

        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

        self.filename = f"{self.output_path}/{self.filename}"
        self.cn = ClassNote(openai_client=self.client, filename=self.filename, subject=self.subject)

    def record_class(self):
        r = AudioRecord(
            filename=f"{self.filename}.wav",
            seconds=self.class_duration)
        r.record()

    def transcribe(self):
        t = Transcribe(self.client, f"{self.filename}.wav")
        t.create_transcript(filename=self.filename)

    def summarize(self):
        self.cn.summarize()

    def create_class_notes(self):
        self.cn.create_notes_collection()

    def debug(self):
        pass
