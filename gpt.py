import os
from openai import OpenAI

client = OpenAI(
    api_key="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",
)

with open("read.txt", encoding="utf8") as file:
    chat_content = file.read()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Get the important topics from the following lecture and list them \n "+chat_content,
        }
    ],
    model="gpt-3.5-turbo",
)

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

    with open("final_output.txt", "a+", encoding="utf8") as final_output:
        final_output.write(class_note.choices[0].message.content)
        final_output.write("\n")