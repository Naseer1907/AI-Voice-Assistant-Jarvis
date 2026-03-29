import pyautogui
import speech_recognition as sr
import phonenumbers

def make_call(name_or_number, country_code):
  phone_number = phonenumbers.parse(name_or_number, country_code)
  pyautogui.click(611, 97)  # Click on the Phone Link icon in the taskbar.
  pyautogui.typewrite(phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164))  # Type in the phone number.
  pyautogui.press('enter')  # Press Enter to make the call.

def get_name_or_number():
  recognizer = sr.Recognizer()
  with sr.Microphone() as mic:
    recognizer.adjust_for_ambient_noise(mic)
    print('Speak the name or phone number of the person you want to call:')
    audio = recognizer.listen(mic)

  try:
    name_or_number = recognizer.recognize_google(audio)
    print('The name or number you spoke is:', name_or_number)
    return name_or_number
  except sr.UnknownValueError:
    print('Sorry, I could not understand your voice.')
    return None

if __name__ == '__main__':
  country_code = 'US'  # The country code for the phone number you want to call.
  name_or_number = get_name_or_number()
  if name_or_number is not None:
    make_call(name_or_number, country_code)
