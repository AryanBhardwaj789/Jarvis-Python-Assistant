# Jarvis Python Assistant

## Description

Jarvis is a voice-activated virtual assistant designed to perform various tasks such as web browsing, playing music and responding to user queries using OpenAI's GPT-3.5-turbo model. It's inspired by AI assistants like Alexa or Google Assistant, providing a wide range of functionalities through voice commands.

## Features

- **Voice Recognition**
  - Utilizes the `speech_recognition` library to listen for and recognize voice commands.
  - Activates upon detecting the wake word "Jarvis."

- **Text-to-Speech**
  - Converts text to speech using `pyttsx3` for local conversion.
  - Uses `gTTS` (Google Text-to-Speech) and `pygame` for playback.

- **Web Browsing**
  - Opens websites like Google, Facebook, YouTube, and LinkedIn based on voice commands.

- **Music Playback**
  - Interfaces with a `musicLibrary` module to play songs via web links.

- **News Fetching**
  - Fetches and reads the latest news headlines using NewsAPI.

- **OpenAI Integration**
  - Handles complex queries and generates responses using OpenAI's GPT-3.5-turbo.
  - Acts as a general virtual assistant for a wide range of queries.

## Workflow

1. **Initialization**
   - Greets the user with "Initializing Jarvis...."

2. **Wake Word Detection**
   - Listens for the wake word "Jarvis."
   - Acknowledges activation by saying "Ya."

3. **Command Processing**
   - Processes commands to determine actions such as opening a website, playing music, fetching news, or generating a response via OpenAI.

4. **Speech Output**
   - Provides responses using the `speak` function with either `pyttsx3` or `gTTS`.

## Libraries Used

- `speech_recognition`: For voice recognition
- `webbrowser`: For opening websites
- `pyttsx3`: For text-to-speech conversion
- `musicLibrary`: Custom module for music playback
- `requests`: For making HTTP requests
- `openai`: For integrating with OpenAI's GPT-3.5-turbo
- `gTTS`: For Google Text-to-Speech
- `pygame`: For audio playback
- `os`: For operating system related operations

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/AryanBhardwaj789/Jarvis-Python-Assistant.git
   cd Jarvis-Python-Assistant
   ```

2. Install the required libraries:
   ```
   pip install speech_recognition webbrowser pyttsx3 requests openai gTTS pygame
   ```

3. Set up your OpenAI API key in an environment variable or configuration file.

4. Run the main script:
   ```
   python jarvis.py
   ```

## Usage

1. Run the script and wait for the initialization message.
2. Say "Jarvis" to activate the assistant.
3. After hearing "Ya," speak your command or question.
4. Jarvis will process your request and respond accordingly.

## Contributing

Contributions to improve Jarvis are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- OpenAI for providing the GPT-3.5-turbo model
- All the creators and maintainers of the libraries used in this project