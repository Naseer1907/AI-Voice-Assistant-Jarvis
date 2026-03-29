import speech_recognition as sr
import pyttsx3
import time
import webbrowser
import sys
import os
import platform
from googleapiclient.discovery import build





API_KEY = "AIzaSyCRm-9dLvoLG3cSvTdmrRBRLj5oyvCkGTo"

def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.say(audio)
    engine.runAndWait()

def open_youtube():
    url = "https://www.youtube.com"
    webbrowser.open(url)
    print("YouTube opened successfully!")

def search_on_youtube(query):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    search_response = youtube.search().list(
        q=query,
        part='id',
        maxResults=5  
    ).execute()

    video_ids = []
    for item in search_response.get('items', []):
        video_id = item.get('id', {}).get('videoId')
        if video_id:
            video_ids.append(video_id)

    if len(video_ids) >= 2:
        video_url = f"https://www.youtube.com/watch?v={video_ids[1]}"  # Play the second video
        webbrowser.open(video_url)
        print("Playing the First video on YouTube...")
    else:
        print("No video found or insufficient videos to play.")

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.energy_threshold = 300
        audio = recognizer.listen(source, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
    except sr.RequestError:
        print("Sorry, I couldn't reach the speech recognition service.")

    return ""

def perform_youtube_search():
    open_youtube()

    exit_commands = ["exit", "quit", "stop"]
    while True:
        speak("What video do you want to search on YouTube?")
        query = listen_command()

        if query:
            if query.lower() in exit_commands:
                speak("Exiting YouTube search. Goodbye!")
                close_web_browser()
                sys.exit()
                break

            search_on_youtube(query)
            time.sleep(10)
        else:
            speak("Sorry, I couldn't understand your query. Please try again.")
def close_web_browser():
    system = platform.system()
    if system == "Windows":
        os.system("taskkill /f /im chrome.exe")  
    elif system == "Darwin":  
        os.system("pkill -f 'Google Chrome'")  
    elif system == "Linux":
        os.system("pkill chrome")  
    else:
        print("Unable to close the web browser. Please close it manually.")

perform_youtube_search()

perform_youtube_search()
