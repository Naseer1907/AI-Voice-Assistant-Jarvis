import webbrowser
import os
import speech_recognition as sr
import pyttsx3


def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.say(audio)
    engine.runAndWait()


def open_google_maps(location):
    search_url = f"https://www.google.com/maps/search/{location}"
    webbrowser.open(search_url)

def search_location(location):
    # Implement the code to open Google Maps with the provided location query
    search_url = f"https://www.google.com/maps/search/{location}"
    webbrowser.open(search_url)
    pass


if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        try:
            speak("Listening for a location...")
            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            user_input = recognizer.recognize_google(audio)
            print(f"Recognized: {user_input}")

            if user_input.lower() == "exit":
                speak("Exiting the program. Goodbye!")
                break

            speak(f"Searching for {user_input} on Google Maps.")
            open_google_maps(user_input)
        except sr.UnknownValueError:
            print("Sorry, couldn't understand your voice.")
        except KeyboardInterrupt:
            break
