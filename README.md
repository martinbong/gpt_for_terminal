# To allow this project to work by simply typing 'chat' in Tilix (zsh) the following things need to be done:

**Make sure the correct dependencies are installed in the virtual environment**
> source .venv/bin/activate  
> pip install -r requirements.txt  
> pip list  

**Create .env needed for keys**
> touch .env  

Add keys to .env:
> export AZURE_OPENAI_API_KEY="KEY"  
> export AZURE_OPENAI_ENDPOINT="URL"  

**Make all .sh files executable (replace '+' by '-' to undo)**
> chmod +x ~/Dev/python/gpt_for_terminal/start_chat.sh  
> chmod +x ~/Dev/python/gpt_for_terminal/activate_env.sh  
> chmod +x ~/Dev/python/gpt_for_terminal/deactivate_env.sh  

> chmod +x ~/Dev/python/gpt_for_terminal/start_mastermind.sh  

**Make Tilix main terminal so it can open using ctrl + alt + t**
> sudo update-alternatives --config x-terminal-emulator  

**Edit ZSH file to create a path to call function from anywhere**
> nano ~/.zshrc  

Add to .zshrc:
> export PATH="$PATH:/home/martin/Dev/python/gpt_for_terminal"  
> alias "chat"="~/Dev/python/gpt_for_terminal/start_chat.sh" 

> alias "mastermind"="~/Dev/python/gpt_for_terminal/start_mastermind.sh"  

Initialize changes:
> source ~/.zshrc  

**Run chat, Quit chat, and Quit chat + Deleting conversation history**
> chat  
> x  
> xx  

> mastermind  
> x  