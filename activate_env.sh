#!/bin/zsh

# Activate the virtual environment
source ~/Dev/python/gpt_for_terminal/venv/bin/activate

# Load environment variables from .env file
set -o allexport
source ~/Dev/python/gpt_for_terminal/.env
set +o allexport
