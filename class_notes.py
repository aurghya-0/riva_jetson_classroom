from datetime import datetime
from custom_logger import getLogger

class ClassNote:
    """
    Class notes class implementing transcription, summarization and creating notes for each topic,
    then compiling them to a list, and finally returning the created list.
    """
    def __init__(self, openai_client, subject):
        self.client = openai_client
        self.subject = subject
        self.log = getLogger()

    def summarize(self, transcription) -> str:
        """Create a summary for the given transcription

        Args:
            transcription (str): transcription to summarize

        Returns:
            str: summary of the transcription
        """
        self.log.info("> Summarizing the transcription....")
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Get the important topics from the following lecture and list them \n " + transcription,
                }
            ],
            model="gpt-3.5-turbo",
        )
        self.log.info("> Summarizing complete....")
        print(chat_completion.choices[0].message.content)

        return chat_completion.choices[0].message.content

    def create_class_note(self, topic_name):
        """Create a class note from a given topic

        Args:
            topic_name (str): name of the topic to create a class note of

        Returns:
            str: Class note for the given topic
        """
        self.log.info(f">> Creating class notes for {topic_name}....")
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Make a detailed university level class note with detailed explanations, equations ("
                               f"if applicable), and examples on the topic of {topic_name}, and format it with "
                               f"markdown.",
                }
            ],
            model="gpt-3.5-turbo",
        )

        self.log.info(f">>> Class notes for {topic_name} created....")

        return chat_completion.choices[0].message.content

    def create_notes_collection(self, topics):
        """
        Create a new collection of notes
        :param topics:
        :return:
        """
        class_notes = []
        for topic in topics:
            class_note = self.create_class_note(topic)
            class_notes.append(class_note)
        
        return class_notes
