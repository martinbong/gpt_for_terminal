# Chat with openai through terminal

**Setup:**
> pip install -r requirements.txt  

**Make secrets available by adding the key and url in .env and exporting the secrets:**
> touch .env  
> export AZURE_OPENAI_API_KEY="KEY"  
> export AZURE_OPENAI_ENDPOINT="URL"  

**Make all .sh files executable (replace '+' by '-' to undo):**
> chmod +x ~/Dev/python/gpt_for_terminal/start_chat.sh  
> chmod +x ~/Dev/python/gpt_for_terminal/start_mastermind.sh

**Edit ZSH file to create a path to call function from anywhere:**
> nano ~/.zshrc  

_**Add to .zshrc:**_
> export PATH="$PATH:/home/martin/Dev/python/gpt_for_terminal"  
> alias "chat"="~/Dev/python/gpt_for_terminal/start_chat.sh"
> alias "mastermind"="~/Dev/python/gpt_for_terminal/start_mastermind.sh"  

**Initialize changes**
> source ~/.zshrc  

**Run chat, Quit chat, and Quit chat + Deleting conversation history:**
> chat  
> x  
> xx  

> mastermind  
> x  