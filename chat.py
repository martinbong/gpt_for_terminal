import os
import json
from openai import AzureOpenAI

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01"
)

# Path to store the conversation history
history_file = "conversation_history.json"

# Function to load conversation history
def load_conversation_history():
    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            return json.load(file)
    return [{"role": "system", "content": "You are a helpful assistant who is a computer expert, that always aims to provide the most to the point and concise answer possible. Whenever the question is about a 'command', assume the tillix terminal using zsh and when a question is about a 'shortcut', assume ubuntu, unless specified otherwise."}]

# Function to save conversation history
def save_conversation_history(history):
    with open(history_file, "w") as file:
        json.dump(history, file)

# Function to delete conversation history
def delete_conversation_history():
    if os.path.exists(history_file):
        os.remove(history_file)

# Function to interact with the GPT model
def chat_with_gpt():
    conversation_history = load_conversation_history()

    welcome_message = "You can chat now! ('x' = quit and 'xx' = quit + delete conversation history)"
    print(welcome_message)

    while True:
        user_input = input("> ")
        if user_input.lower() == "x":
            save_conversation_history(conversation_history)
            break
        elif user_input.lower() == "xx":
            delete_conversation_history()
            break

        conversation_history.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="intelligence-gpt35",
            messages=conversation_history
        )

        ai_response = response.choices[0].message.content
        print("________________________________________________________________________________________________________________________________________")
        print(f"GPT: {ai_response}")
        print("________________________________________________________________________________________________________________________________________")

        conversation_history.append({"role": "assistant", "content": ai_response})


if __name__ == "__main__":
    chat_with_gpt()
