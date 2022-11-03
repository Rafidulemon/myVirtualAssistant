import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import pyjokes
from datetime import date
import wikipedia
import webbrowser
import os
import smtplib
import googletrans
import gtts
import playsound

r = sr.Recognizer()
translator = googletrans.Translator()
translate_to = 'ja'
greetings = ['good morning', 'good afternoon', 'good evening', 'good night']
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
talk("Hello. How can i help you?")

def take_command():
    try:
        with sr.Microphone(device_index=2) as source:
            r.adjust_for_ambient_noise(source, duration=1)
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

def greeting():
    now = datetime.datetime.now()
    hour = now.hour

    if hour < 12:
        greeting = "good morning"
    elif hour < 18:
        greeting = "good afternoon"
    else:
        greeting = "good evening"
    return greeting

def trans():
    talk("I can only translate to Japanese language now. Now tell me what should i translate.")
    content = take_command()
    translated = translator.translate(content, dest='ja')
    trans = translated.text
    print(trans)
    audio = gtts.gTTS(translated.text, lang=translate_to)
    audio.save('audio.mp3')
    playsound.playsound('audio.mp3')

def openBrowser(command):
    if 'youtube' in command:
        talk("Opening youtube for you")
        webbrowser.open("https://www.youtube.com/")
    elif 'google' in command:
        talk("Opening google for you")
        webbrowser.open("google.com")
    elif 'facebook' in command:
        talk("Opening facebook for you")
        webbrowser.open("facebook.com")
    elif 'linkedin' in command:
        talk("Opening linkedin for you")
        webbrowser.open("https://www.linkedin.com/")
    elif 'android studio' in command:
        talk("Opening android studio for you")
        path = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
        os.startfile(path)
    else:
        print("URL not found")
        talk("URL not found")

def openEmail():
    try:
        talk("Tell me the email address")
        to = take_command()
        talk("What should I say")
        content = take_command()
        sendEmail(to,content)
        talk("Email has been sent!")
    except Exception as e:
        #print(e)
        talk("I am not able to send this email")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('rafid.nexkraft@gmail.com', 'password')
    server.sendmail('rafid.nexkraft@gmail.com', to, content)
    server.close()

def run():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('It is'+time)
    elif 'date' in command:
        today = date.today().strftime("%d/%m/%Y")
        talk('Today is '+today)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing '+song)
        pywhatkit.playonyt(song)
    elif 'hello' in command:
        greet = greeting()
        talk('Hello '+greet)
    elif command in greetings:
        if 'good night' in command:
            print("Exiting..")
            talk("Thank you. Good Bye")
            exit()
        for g in greetings:
            if g in command:
                greet = greeting()
                if command != greet:
                    talk('Sorry. It is '+greet+' now')
                else:
                    talk(greet)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'thank you' in command:
        talk('You are most welcome')
    elif 'who are you' in command:
        talk('I am your virtual assistant')
    elif 'your name' in command:
        talk('I do not have any name. But you can call me dear')
    elif 'are you single' in command:
        talk('Opps!! Machine can not be in relationship.')
    elif 'how are you' in command:
        talk('I am fine. What about you?')
    elif 'I am fine' in command:
        talk('Good to know that.')
    elif 'I love you' in command:
        talk('Ha ha ha    Good to know that. I also love you.')
    elif 'wikipedia' in command:
        talk("Searching wikipedia")
        command = command.replace('wikipedia', '')
        result = wikipedia.summary(command, sentences=1)
        print(result)
        talk(result)
    elif 'open' in command:
        openBrowser(command)

    elif 'send email' in command:
        openEmail()
    elif 'translate' in command:
        trans()
    elif 'exit' in command:
        print("Exiting..")
        talk("Thank you. Good Bye for now")
        exit()
    elif 'None' in command:
        print("Error occoured")
    else:
        talk('I did not get you. But I am going to search it for you')
        pywhatkit.search(command)
while True:
    run()