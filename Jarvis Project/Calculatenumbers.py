import speech_recognition as sr
import pyttsx3
import operator

# Define a mapping for spoken phrases to operators
operator_mapping = {
    "plus": "+",
    "minus": "-",
    "multiply": "*",
    "divided by": "/",
    "to the power of": "**",
}

def listen_for_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("Command:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your command.")
    except sr.RequestError as e:
       print(f"Could not request results from Google Speech Recognition service: {e}")


def interpret_command(command):
    # Replace spoken phrases with corresponding operators
    for phrase, op in operator_mapping.items():
        command = command.replace(phrase, op)

    # Replace 'x' with '*' to handle '2 x 5' as '2 * 5'
    command = command.replace('x', '*')
    return command


def calculate(expression):
    try:
        result = eval(expression)
        print("Result:", result)
        return result
    except (SyntaxError, NameError, ZeroDivisionError, TypeError) as e:
        print("Invalid expression:", e)

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def calculator_voice():
    while True:
        command = listen_for_command()
        if command == 'quit':
            speak("Goodbye sir!")
            break
        command = interpret_command(command)
        result = calculate(command)
        speak("The result is: " + str(result))

# Run the calculator with voice input and audible output
calculator_voice()
