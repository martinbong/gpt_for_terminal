import os
import sys
import json
import time
import tty
import termios
import threading
import select
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01"
)

history_file = "conversation_history.json"

def load_conversation_history():
    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            return json.load(file)
    return [{
        "role": "system",
        "content": "You are a helpful assistant who is a computer expert, that always aims to provide the most to the point and concise answer possible. Whenever the question is about a 'command', assume the tilix terminal using zsh and when a question is about a 'shortcut', assume ubuntu, unless specified otherwise."
    }]

def save_conversation_history(history):
    with open(history_file, "w") as file:
        json.dump(history, file)

def delete_conversation_history():
    if os.path.exists(history_file):
        os.remove(history_file)

def disable_input():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setcbreak(fd)
    return fd, old_settings

def enable_input(fd, old_settings):
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def flush_input():
    while select.select([sys.stdin], [], [], 0)[0]:
        os.read(sys.stdin.fileno(), 1024)

class Spinner:
    def __init__(self, message="Thinking..."):
        self.spinner_chars = ['|', '/', '-', '\\']
        self.running = False
        self.thread = None
        self.message = message

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._spin)
        self.thread.start()

    def _spin(self):
        i = 0
        while self.running:
            sys.stdout.write(f"\r\033[92m{self.spinner_chars[i % 4]} {self.message}\033[0m")
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()
        sys.stdout.write("\r" + " " * 80 + "\r")
        sys.stdout.flush()

def read_full_input(prompt="> "):
    WHITE = "\033[97m"
    RESET = "\033[0m"
    sys.stdout.write(f"{WHITE}{prompt}")
    sys.stdout.flush()

    os.write(sys.stdout.fileno(), WHITE.encode())

    buffer = []
    fd = sys.stdin.fileno()

    while True:
        rlist, _, _ = select.select([fd], [], [], None)
        if rlist:
            chunk = os.read(fd, 1024).decode()
            buffer.append(chunk)
            break

    while True:
        rlist, _, _ = select.select([fd], [], [], 0.1)
        if rlist:
            chunk = os.read(fd, 1024).decode()
            buffer.append(chunk)
        else:
            break

    # Reset terminal color after input
    os.write(sys.stdout.fileno(), RESET.encode())

    return "".join(buffer).strip()


def chat_with_gpt():
    conversation_history = load_conversation_history()
    print("You can chat now! ('x' = quit, 'xx' = quit + delete history)")

    while True:
        user_input = read_full_input("> ")

        if not user_input.strip():
            continue

        normalized_input = user_input.lower()
        if normalized_input == "x":
            save_conversation_history(conversation_history)
            break
        elif normalized_input == "xx":
            delete_conversation_history()
            break

        conversation_history.append({"role": "user", "content": user_input})

        fd, old_settings = disable_input()
        spinner = Spinner()
        spinner.start()

        try:
            response = client.chat.completions.create(
                model="intelligence-gpt4o",
                messages=conversation_history
            )
        finally:
            spinner.stop()
            enable_input(fd, old_settings)
            flush_input()

        ai_response = response.choices[0].message.content.strip()
        print(f"\033[92m{ai_response}\033[0m")

        try:
            width = os.get_terminal_size().columns
        except OSError:
            width = 80
        print('─' * width)

        conversation_history.append({"role": "assistant", "content": ai_response})

if __name__ == "__main__":
    chat_with_gpt()
