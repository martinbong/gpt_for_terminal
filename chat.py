import os
from openai import AzureOpenAI

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01"
)


# Function to interact with the GPT model
def chat_with_gpt():
    conversation_history = [{"role": "system", "content": "You are a helpful assistant who is a computer expert, that always aims to provide the to the point and concise answer possible. Whenever the question is about a 'command', assume the tillix terminal using zsh and when a question is about a 'shortcut', assume ubuntu, unless specified otherwise."}]

    while True:
        user_input = input("> ")
        if user_input.lower() == "x":
            break

        conversation_history.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="intelligence-gpt35",
            messages=conversation_history
        )

        ai_response = response.choices[0].message.content
        print(f"{ai_response}")

        conversation_history.append({"role": "assistant", "content": ai_response})


if __name__ == "__main__":
    chat_with_gpt()
