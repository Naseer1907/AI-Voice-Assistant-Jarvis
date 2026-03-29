import time
import webbrowser
import pyttsx3
import speech_recognition as sr
import sys
import os
import platform

def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.say(audio)
    engine.runAndWait()

def open_google_search():
    url = "https://www.google.com"
    webbrowser.open(url)
    print("Google search opened successfully!")

def search_on_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    print(f"Searching for '{query}' on Google...")

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

def perform_google_search():
    open_google_search()

    exit_commands = ["exit", "quit", "stop"]
    while True:
        speak("What topic do you want to search on Google?")
        query = listen_command()

        if query:
            if query in exit_commands:
                speak("Exiting Google search. Goodbye!")
                close_web_browser()
                sys.exit()
                break

            search_on_google(query)
            time.sleep(3)
        else:
            speak("Sorry, I couldn't understand your query. Please try again.")

def close_web_browser():
    system = platform.system()
    if system == "Windows":
        os.system("taskkill /f /im chrome.exe")  # Close Google Chrome
    elif system == "Darwin":  # macOS
        os.system("pkill -f 'Google Chrome'")  # Close Google Chrome
    elif system == "Linux":
        os.system("pkill chrome")  # Close Google Chrome
    else:
        print("Unable to close the web browser. Please close it manually.")

perform_google_search()

perform_google_search()
