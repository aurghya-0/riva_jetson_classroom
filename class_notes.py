from datetime import datetime


class ClassNote:
    def __init__(self, openai_client, filename, subject):
        self.client = openai_client
        self.subject = subject
        self.filename = filename

    def summarize(self, transcription):
        # Create a chat completion and output the result to a file
        print("> Summarizing the transcription....")
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Get the important topics from the following lecture and list them \n " + transcription,
                }
            ],
            model="gpt-3.5-turbo",
        )
        print("> Summarizing complete....")
        print(chat_completion.choices[0].message.content)

        return chat_completion.choices[0].message.content

    def create_class_note(self, chat_content):
        print(f">> Creating class notes for {chat_content}....")
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Make a detailed university level class note with detailed explanations, equations (if applicable), and examples on the topic of {chat_content}, and format it with markdown.",
                }
            ],
            model="gpt-3.5-turbo",
        )

        print(f">>> Class notes for {chat_content} created....")

        return chat_completion.choices[0].message.content

    def create_notes_collection(self, topics):
        class_notes = []
        for topic in topics:
            class_note = self.create_class_note(topic)
            class_notes.append(class_note)
        
        return class_notes
