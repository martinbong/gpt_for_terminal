#!/bin/zsh
# Activate the environment
source ~/Dev/python/gpt_for_terminal/activate_env.sh

# Run the chat script
python3 ~/Dev/python/gpt_for_terminal/chat.py

# Source the deactivation script after the Python script ends
source ~/Dev/python/gpt_for_terminal/deactivate_env.sh