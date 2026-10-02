from openai import OpenAI

client = OpenAI()

print("Welcome to AI Study Buddy!")

with open("notes.txt", "r") as file:
    notes = file.read()

question = input("\nWhat would you like to know? ")

response = client.responses.create(
    model="gpt-5-mini",
    instructions="Answer the user's question using the study notes provided. If the answer is not in the notes, say that you don't know based on the notes.",
    input=f"""
Study notes:

{notes}

Student question:

{question}
"""
)

print("\nAnswer:")
print(response.output_text)