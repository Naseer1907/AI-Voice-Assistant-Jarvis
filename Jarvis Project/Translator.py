from gtts import gTTS
import pyttsx3
import speech_recognition as sr
import os
import time
import pygame
from deep_translator import GoogleTranslator

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Change to desired voice
engine.setProperty("rate", 170)  # Adjust speech speed

# Initialize pygame mixer for playing sound
pygame.mixer.init()

# Function to speak the given text using pyttsx3
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to listen and recognize speech
def takeCommand(prompt=False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if prompt:
            speak(prompt)
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("Listening timed out. Try speaking again.")
            return "None"

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "None"
    except Exception as e:
        print(f"Error: {e}")
        return "None"
    
    return query

# Function to translate the given text to the selected language and speak it using gTTS
def translategl(query, dest_lang):
    try:
        translator = GoogleTranslator(source='auto', target=dest_lang)
        translated_text = translator.translate(query)
        print(f"Translated Text: {translated_text}")
        
        # Use gTTS to convert text to speech
        tts = gTTS(text=translated_text, lang=dest_lang, slow=False)
        
        # Generate a unique filename based on current timestamp
        timestamp = time.strftime("%Y%m%d%H%M%S")
        filename = f"voice_{timestamp}.mp3"
        
        tts.save(filename)

        # Play the audio file using pygame
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        
        # Remove the temporary mp3 file after playing
        if os.path.exists(filename):
            os.remove(filename)
    except Exception as e:
        print(f"Unable to translate: {e}")

if __name__ == "__main__":
    speak("Welcome! Let's get started.")

    # Select language for translation
    speak("Choose the language in which you want to translate. For example, say 'Hindi' or 'French'.")
    lang_choice = takeCommand("Please say the language you want to translate to, like 'Hindi' or 'French'.").lower()

    # Create a GoogleTranslator instance to access supported languages
    translator_instance = GoogleTranslator()

    # Supported language codes for Indian languages and others
    lang_code_dict = {
        'english': 'en',
        'hindi': 'hi',
        'kannada': 'kn',
        'telugu': 'te',
        'tamil': 'ta',
        'bengali': 'bn',
        'french': 'fr',
        'german': 'de',
        'spanish': 'es'
    }

    # Check if the language is supported, and get the corresponding language code
    lang_code = lang_code_dict.get(lang_choice, "en")

    if lang_code == "en":
        speak("Sorry, I did not recognize that language. Defaulting to English.")
    else:
        speak(f"Translating to {lang_choice.capitalize()}. You can start speaking now.")

    while True:
        query = takeCommand("Start speaking to translate, say 'stop' to end.")
        if query and query.lower() == "stop":
            speak("Translation stopped. Goodbye!")
            break
        elif query and query.lower() != "none":
            translategl(query, lang_code)
