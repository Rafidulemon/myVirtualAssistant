import datetime

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 190)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def dateDetails(command):
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('It is'+time)
    elif 'date' in command:
        today = datetime.datetime.now().strftime('%B %d,%Y')
        print(today)
        talk('Today is '+today)
    elif 'weekday' in command:
        today = datetime.datetime.now().strftime('%A')
        print(today)
        talk('Today is '+today)