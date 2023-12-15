from openai_client import OpenAIKey
from openai import OpenAI
from audio_record import AudioRecord
from whisper_transcribe import Transcribe
from datetime import datetime
from class_notes import ClassNote
from mongodb_config import get_database
import os


# - Add a way to get the class duration from the user
# - Add a way to get the class name from the user
# - Organize the files into folders
# - Move everything to a database based system

class Classroom:
    """Main class implementing the functionalities of classroom recording, 
    transcribing, summarizing and then generating the notes for the topics"""

    def __init__(self, class_name, class_duration=10, subject="HPC"):
        self.client = OpenAI(api_key=OpenAIKey.key)
        self.DEBUG = False
        self.now = datetime.now()
        self.filename = self.now.strftime(f"%d-%m-%Y-%H-%M-%S - {class_name}")
        self.class_name = class_name
        self.class_duration = class_duration
        self.subject = subject
        self.db = get_database()
        self.collection = self.db["transcriptions"]
        self.cn = ClassNote(openai_client=self.client, 
                            filename=self.filename, subject=self.subject)

    def record_class(self):
        r = AudioRecord(
            filename=f"{self.filename}.wav",
            seconds=self.class_duration)
        r.record()

    def transcribe(self):
        # TODO - Create MP3 instead of WAV and send it in chunks, need to test

        # DEBUG BLOCK
        # with open("text.txt", "r") as file:
        #     self.transcript = file.read()

        t = Transcribe(self.client, f"{self.filename}.wav")
        transcript = t.create_transcript(filename=self.filename)        
        os.remove(f"{self.filename}.wav")
        transcript_item = {
            "transcript": transcript,
            "subject": self.subject,
            "class_name": self.class_name
        }
        return transcript_item

    def summarize(self):
        transcript_item = self.transcribe()
        summarization = self.cn.summarize(transcript_item["transcript"])
        transcript_item["summarization"] = summarization
        return transcript_item

    def create_class_notes(self):
        # TODO : Create a channel from summarize to create class notes
        summarization = self.summarize()
        topics = summarization["summarization"].split("\n")
        class_notes = self.cn.create_notes_collection(topics)
        summarization["class_notes"] = class_notes
        self.collection.insert_one(summarization)

    def debug(self):
        pass
