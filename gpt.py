import os
from openai import OpenAI

# Debug mode
DEBUG_MODE = False

# OpenAI Client Setup
client = OpenAI(
    api_key="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",
)

# Open or create the file for reading the transcript 
with open("read.txt", encoding="utf8") as file:
    chat_content = file.read()

# Create a chat completion and output the result to a file
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Get the important topics from the following lecture and list them \n "+chat_content,
        }
    ],
    model="gpt-3.5-turbo",
)

if DEBUG_MODE == True:
    print(chat_completion.choices[0].message.content)

with open ("output.txt", "w", encoding="utf8") as output:
    output.write(chat_completion.choices[0].message.content)

with open ("output.txt", "r", encoding="utf8") as input:
    topics = input.readlines()


print(topics)

for topic in topics:
    class_note = client.chat.completions.create(
        messages=[
            {
                "role" : "user",
                "content": "Make a detailed university level class note with sufficient explanations and sample questions on the topic of " + topic
            }
        ],
        model="gpt-3.5-turbo",
    )

    if DEBUG_MODE == True:
        print(class_note.choices[0].message.content)
        print("\n\n")

    with open("final_output.txt", "a+", encoding="utf8") as final_output:
        final_output.write(class_note.choices[0].message.content)
        final_output.write("\n\n")