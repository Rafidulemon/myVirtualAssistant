import speech_recognition as sr
import pyttsx3
import requests
from bs4 import BeautifulSoup


r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 190)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening")
            voice = r.listen(source,timeout=5, phrase_time_limit=5)
            result = r.recognize_google(voice, language='en')
            result = result.lower()
            print("Did you say "+"-"+result+"?")
    except Exception as ex:
        #print(ex)
        print('Say it again')
        return "None"
    return result

def Temperature():
    search = "temperature in dhaka"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temperature = data.find("div", class_="BNeawe").text
    talk(f"The Temperature Outside Is {temperature} celcius")
    Current_Level = data.find(class_='IsqQVc_NprOob_XcVN5d')
    print(Current_Level)
    print(temperature)

    talk("Do I Have To Tell You Another Place Temperature ?")
    next = take_command()

    if 'yes' in next:
        talk("Tell Me The Name Of tHE Place ")
        name = take_command()
        search = f"temperature in {name}"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temperature = data.find("div", class_="BNeawe").text
        talk(f"The Temperature in {name} is {temperature} celcius")

    else:
        talk("no problem sir")