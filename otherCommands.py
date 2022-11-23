import pyttsx3
import pywhatkit
import pyjokes
import speech_recognition as sr
import datetime
import psutil
import webbrowser

r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 190)
name = ''

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone(device_index=1) as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print("Listening")
            voice = r.listen(source, timeout=5, phrase_time_limit=5)
            result = r.recognize_google(voice, language='en')
            result = result.lower()
            print("Did you say " + "-" + result + "?")
    except Exception as ex:
        print(ex)
        #print('Say it again')
        return "None"
    return result

def myName():
    talk("Are you Mr. Raafeed Sir?")
    command = take_command()
    if 'yes' in command:
        talk("See.. I know your name Sir")
    else:
        talk("May I know your name?")
        name = take_command()
        talk("OK " + name + " Sir! Nice to meet you ! How do you know Raafeed sir?")
        c = take_command()
        talk("Oh! I see.. What can i do for you "+ c + " Sir?")

def battery():
    battery = psutil.sensors_battery()
    parcen = battery.percent
    if parcen == 100:
        talk("Sir! Our system is fully charged")
    elif parcen<30:
        talk("Sir! Our system has only" + str(parcen) + " percent battery health. You should plug in the charger.")
    else:
        talk("Sir! Our system has " + str(parcen) + " percent battery health")

def functions():
    count = 22
    talk("Sir, Currently I have  "+ str(count) + " functions. I am still learning. Hopefully I will be able to come up with more functions")

def ageCal():

    today = datetime.datetime.now().date()
    dob = datetime.date(2022, 11, 1)
    age = int((today - dob).days / 365.25)
    talk("I am "+str(age)+" years old SIR!")
    talk("I was created by Mr. Raafeedul Islam on first November, 2022")

def other(command):
    if 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'thank you' in command:
        talk('You are most welcome Sir!')
    elif 'who are you' in command or 'yourself' in command or 'tell me about you' in command:
        talk('Ok Sir! I am Aliza, the virtual assistant. I was developed by Mr Raafeedul Islam.')
        talk('I can assist you for any kind of software level task, like, searching something, opening or closing apps, telling jokes, playing mmusic or video and so on')
        talk('I am using GUI by qt5.')
        talk('That is all about me Sir! Now tell me how can i help you')
    elif 'your name' in command:
        talk('I am your virtual assistant Aliza.')
    elif 'are you single' in command:
        talk('Opps!! Machine can not be in relationship.')
    elif 'how are you' in command:
        talk('I am fine Sir. What about you?')
    elif 'i am fine' in command:
        talk('Good to know that.')
    elif 'i love you' in command:
        talk('Ha ha ha    Good to know that. But I am a machine and Sir! and you have girlfriend.')
    elif 'what are you doing now' in command:
        talk("Talking to you sir!")
    elif 'how old are you' in command:
        ageCal()
    elif 'what is my name' in command:
        myName()
    elif 'are you free' in command:
        talk('No Sir! I am available now, but not free')
    elif 'who is anika' in command:
        talk('Sir! Anika maam is your wife.')
    elif 'how many functions' in command or 'your functions' in command or 'how many features' in command \
            or 'your features' in command:
        functions()
    elif 'battery' in command:
        battery()
    elif 'internet speed' in command:
        webbrowser.open("https://fast.com/")
    else:
        talk('I did not get you. But I am going to search it for you')
        pywhatkit.search(command)

command = take_command()
other(command)