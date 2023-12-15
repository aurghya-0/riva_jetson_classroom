from openai_client import OpenAIKey
from openai import OpenAI
from audio_record import AudioRecord
from whisper_transcribe import Transcribe
from datetime import datetime
from class_notes import ClassNote
from mongodb_config import get_database
from dateutil import parser
import os


# - Add a debug mode
# - Add a way to get the class duration from the user
# - Add a way to get the class name from the user
# - Organize the files into folders
# - Move everything to a database based system

class Classroom:
    """Main class implementing the functionalities of classroom recording, transcribing,
    summarizing and then generating the notes for the topics"""

    def __init__(self, class_name, class_duration=10, subject="HPC"):
        self.transcript = None
        self.client = OpenAI(api_key=OpenAIKey.key)
        self.DEBUG = False
        self.now = datetime.now()
        self.filename = self.now.strftime(f"%d-%m-%Y-%H-%M-%S - {class_name}")
        self.class_name = class_name
        self.class_duration = class_duration
        self.subject = subject
        self.db = get_database()
        self.collection = self.db["transcriptions"]
        self.id = "random"

        self.cn = ClassNote(openai_client=self.client, filename=self.filename, subject=self.subject)

    def record_class(self):
        r = AudioRecord(
            filename=f"{self.filename}.wav",
            seconds=self.class_duration)
        r.record()

    def transcribe(self):
        # t = Transcribe(self.client, f"{self.filename}.wav")
        with open("text.txt", "r") as file:
            self.transcript = file.read()
        # transcript = t.create_transcript(filename=self.filename)
        transcript_item = {
            "transcript": self.transcript,
            "subject": self.subject,
            "class_name": self.class_name
        }
        result = self.collection.insert_one(transcript_item)
        self.id = result.inserted_id

    def summarize(self):
        summarization = self.cn.summarize(self.transcript)
        db_entry = self.collection.find_one(self.id)
        print(db_entry)
        self.collection.update_one({"_id": self.id}, {"$set": {"summary": summarization}})

    def create_class_notes(self):
        # TODO : Create a channel from summarize to create class notes
        self.cn.create_notes_collection()

    def debug(self):
        pass
