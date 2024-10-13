import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv('.env.local')
# Access the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {   "role": "system", 
                "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Home. Give short responses please"
            },
            {
                "role": "user",
                "content": command
            }
        ]
    )
    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis......")
    while True:
        # Listen for the wake word jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("Recognizing......")
        try:
            with sr.Microphone() as source:
                print("Listening......")
                audio = r.listen(source, timeout=10, phrase_time_limit=5)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active......")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))

