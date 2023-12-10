class ClassNote:
    def __init__(self, openai_client, filename):
        self.filename = filename
        self.client = openai_client

    def summarize(self):
        with open(f"{self.filename}.txt", encoding="utf8") as file:
            chat_content = file.read()

        # Create a chat completion and output the result to a file
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Get the important topics from the following lecture and list them \n "+chat_content,
                }
            ],
            model="gpt-3.5-turbo",
        )

        with open (f"{self.filename} - Summary.txt", "w", encoding="utf8") as output:
            output.write(chat_completion.choices[0].message.content)

    def create_class_note(self, chat_content):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Make a detailed university level class note with sufficient explanations and sample questions on the topic of {chat_content}",
                }
            ],
            model="gpt-3.5-turbo",
        )

        return chat_completion.choices[0].message.content

    def create_notes_collection(self):
        with open(f"{self.filename} - Summary.txt", "r", encoding="utf8") as input:
            topics = input.readlines()

        for topic in topics:
            class_note = self.create_class_note(topic)

            with open(f"{self.filename} - Class Notes.txt", "a+", encoding="utf8") as final_output:
                final_output.write(class_note.choices[0].message.content)
                final_output.write("\n\n")
