apt install sudo
sudo apt update
sudo apt install -y python3 python3-pip git build-essential portaudio19-dev \
                   python3-pyaudio nano wget unzip libssl-dev \
                   libffi-dev python3-dev

# Install Python Telegram Bot library
pip install python-telegram-bot==13.7

# Install Google Assistant SDK
pip install google-assistant-sdk[samples]==0.5.0

# Install PyAudio for audio handling
pip install pyaudio==0.2.11

# Install Google API client
pip install google-api-python-client==2.0.2

# Install Python Fire for CLI 
pip install fire==0.4.0

# Install requests for API calls
pip install requests==2.28.1

# Install pytz for timezone handling
pip install pytz==2022.7

# Install click for CLI
pip install click==8.1.3
