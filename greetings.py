import pyttsx3
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def greeting():
    now = datetime.datetime.now()
    hour = now.hour

    if hour>=0 and hour <= 12:
        talk("Good morning, sir")
        #greeting = "good morning"
    elif hour>12 and hour <= 18:
        talk("Good afternoon, sir")
    else:
        talk("Good evening, sir")
    talk("Please tell me, How can I help you ?")