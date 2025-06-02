# To allow this project to work by simply typing 'chat' in Tilix (zsh) the following things need to be done:

**Setup in home folder**
> sudo apt update  
> sudo apt install python3 virtualenv

**Clone project (https)**
> git clone https://github.com/martinbong/gpt_for_terminal.git

**Activate a virtual environment**
> virtualenv venv  
> source venv/bin/activate  

**Make sure the correct dependencies are installed in the virtual environment from within the project folder. Its important to check the interpreter settings**
> which python3  
> pip install -r requirements.txt  
> pip list  

**Create .env needed for keys**
> touch .env  

**Add secrets to .env (UnknownGroup user): https://console.cloud.google.com/run/detail/europe-west4/prod-sp-services/revisions?inv=1&invt=AbzBeA&project=maximal-cider-305010&rapt=AEjHL4OZQMJO2UyWRdlxeayz2uZpxAiair9SYxJcYY1ZHS8W0QuPQ8luYgUoEkn5xsXyWent8SXA9SRrCW8stqHA_3xBjISPhJkkBUmO5JGYk_EYuz8PUVE&authuser=1**
> export AZURE_OPENAI_API_KEY="KEY"  
> export AZURE_OPENAI_ENDPOINT="URL"  

**Make all .sh files executable (replace '+' by '-' to undo)**
> chmod +x ~/Dev/python/gpt_for_terminal/start_chat.sh  
> chmod +x ~/Dev/python/gpt_for_terminal/start_mastermind.sh  

**Make Tilix main terminal so it can open using ctrl + alt + t**
> sudo update-alternatives --config x-terminal-emulator  

**Edit ZSH file to create a path to call function from anywhere**
> nano ~/.zshrc  

**Add to .zshrc:**
> export PATH="$PATH:/home/martin/Dev/python/gpt_for_terminal"  
> alias "chat"="~/Dev/python/gpt_for_terminal/start_chat.sh" 

> alias "mastermind"="~/Dev/python/gpt_for_terminal/start_mastermind.sh"  

**Initialize changes**
> source ~/.zshrc  

**Run chat, Quit chat, and Quit chat + Deleting conversation history**
> chat  
> x  
> xx  

> mastermind  
> x  