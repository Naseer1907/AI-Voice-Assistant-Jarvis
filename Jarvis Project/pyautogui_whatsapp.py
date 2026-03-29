import speech_recognition as sr
import pyttsx3
import time
import pyautogui
import sys
import os
import platform

def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.say(audio)
    engine.runAndWait()

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

def select_recipient(recipient_name):
    # Adjust coordinates based on your system
    search_bar_location = (195, 115)
    search_results_location = (80, 250)
    message_input_location = (188, 249)

    # Open WhatsApp application
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('whatsapp', interval=0.1)
    pyautogui.press('enter')
    time.sleep(5)  # Adjust delay based on your system

    # Search for the recipient
    pyautogui.click(search_bar_location)
    pyautogui.write(recipient_name, interval=0.1)
    time.sleep(2)

    # Select the recipient from the search results
    pyautogui.click(search_results_location)
    time.sleep(2)

    # Return the message input location
    return message_input_location

def send_message(recipient_name, message):
    # Select recipient and get message input location
    message_input_location = select_recipient(recipient_name)

    # Type and send the message
    pyautogui.click(message_input_location)
    pyautogui.write(message, interval=0.1)
    pyautogui.press('enter')

def send_whatsapp_message():
    speak("To whom do you want to send a WhatsApp message?")
    recipient_name = listen_command()
    
    speak("What's the message?")
    message = listen_command()

    if recipient_name and message:
        speak(f"Sending message to {recipient_name}...")
        send_message(recipient_name, message)
        speak("Message sent successfully!")
    else:
        speak("Sorry, I couldn't understand the recipient or the message.")

     
    exit_commands = ["exit", "quit", "stop"]
    while True:
        query = listen_command()
        speak("Are You Sure")
        query = listen_command()
        if 'yes' in query:
                speak("Exiting Whatsapp. Goodbye!")
                close_whatsapp()
                sys.exit()
                break

            
        else:
            speak("Sorry, I couldn't understand your Message. Please try again.")
def close_whatsapp():
    system = platform.system()
    if system == "Windows":
        os.system("taskkill /f /im whatsapp.exe")  
    elif system == "Darwin":  
        os.system("pkill -f 'Google Chrome'")  
    elif system == "Linux":
        os.system("pkill chrome")  
    else:
        print("Unable to close the Whatsapp. Please close it manually.")


        

# Example usage
send_whatsapp_message()
