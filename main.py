import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import pyjokes
import wikipedia
import webbrowser
import os
import smtplib
import googletrans
import gtts
import playsound
import requests
import subprocess
import calendar

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

# from intro import play_gif
# play_gif

def take_command():
    try:
        with sr.Microphone(device_index=1) as source:
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

def greetingCheck(command):
    if 'good night' in command:
        print("Exiting..")
        talk("Thank you. Good Bye")
        exit()
    for g in greetings:
        if g in command:
            greet = greeting()
            if command != greet:
                talk('Sorry. It is ' + greet + ' now')
            else:
                talk(greet)

def greeting():
    now = datetime.datetime.now()
    hour = now.hour

    if hour>=0 and hour <= 12:
        greeting = "good morning"
    elif hour>12 and hour <= 18:
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
    os.remove('audio.mp3')

def openBrowser(command):
    if 'youtube' in command:
        talk("Opening youtube for you")
        webbrowser.open("https://www.youtube.com/")
    elif 'google' in command:
        talk("Opening google for you")
        webbrowser.open("https://www.google.com")
    elif 'facebook' in command:
        talk("Opening facebook for you")
        webbrowser.open("https://www.facebook.com")
    elif 'linkedin' in command:
        talk("Opening linkedin for you")
        webbrowser.open("https://www.linkedin.com/")
    elif 'github' in command:
        talk("Opening github for you")
        webbrowser.open("https://www.github.com/")
    elif 'android studio' in command:
        talk("Opening android studio for you")
        path = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
        os.startfile(path)
    elif 'vs code' in command:
        talk("Opening visual studio for you")
        path = "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path)
    elif 'firefox' in command:
        talk("Opening Mozilla firefox for you")
        path = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
        os.startfile(path)
    elif 'file explorer' in command:
        subprocess.Popen('explorer')
    elif 'c drive' in command:
        print("Opening c drive...")
        talk("Opening c drive sir")
        subprocess.Popen('explorer "C:\"')
    elif 'd drive' in command:
        print("Opening d drive...")
        talk("Opening d drive sir")
        subprocess.Popen('explorer "D:\"')
    elif 'e drive' in command:
        print("Opening e drive...")
        talk("Opening e drive sir")
        subprocess.Popen('explorer "E:\"')
    elif 'f drive' in command:
        print("Opening f drive...")
        talk("Opening f drive sir")
        subprocess.Popen('explorer "F:\"')
    elif 'camera' in command:
        print("Opening camera...")
        talk("Opening camera sir")
        os.system("start microsoft.windows.camera:")
    elif 'calendar' in command:
        talk("For which year sir?")
        yy = int(input("Enter year: "))
        talk("Which month sir?")
        mm = int(input("Enter month: "))
        talk("Thank you sir.Showing calendar..")
        print("Showing calendar...")
        print(calendar.month(yy, mm))
    elif 'zoom' in command:
        talk("Opening zoom for you")
        path = "C:\\Users\\Asus\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
        os.startfile(path)
    elif 'slack' in command:
        talk("Opening slack for you")
        path = "C:\\Users\\Asus\\AppData\\Local\\slack\\slack.exe"
        os.startfile(path)

    else:
        print("URL not found")
        talk("URL not found")

def openEmail():
    try:
        talk("Tell me the email address")
        to = input("Enter receiver email address:")
        talk("What should I say")
        content = take_command()
        sendEmail(to, content)
        talk("Email has been sent!")
    except Exception as e:
        #print(e)
        talk("I am not able to send this email")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('rafid.nexkraft@gmail.com', 'rafid420')
    server.sendmail('rafid.nexkraft@gmail.com', to, content)
    server.close()

def weather():
    talk("Enter the city name please")
    city = input('Enter the city name please')
    talk('Displaying Weather report for: ' + city)
    print('Displaying Weather report for: ' + city)
    url = 'https://wttr.in/{}'.format(city)
    res = requests.get(url)
    print(res.text)

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

def other(command):
    if 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'thank you' in command:
        talk('You are most welcome')
    elif 'who are you' in command:
        talk('I am your virtual assistant')
    elif 'your name' in command:
        talk('I am your virtual assistant Aliza.')
    elif 'are you single' in command:
        talk('Opps!! Machine can not be in relationship.')
    elif 'how are you' in command:
        talk('I am fine. What about you?')
    elif 'i am fine' in command:
        talk('Good to know that.')
    elif 'i love you' in command:
        talk('Ha ha ha    Good to know that. I also love you.')
    elif 'what are you doing now' in command:
        talk("Talking to you sir!")
    elif 'are you free' in command:
        talk('No. I am available now, but not free')
    else:
        talk('I did not get you. But I am going to search it for you')
        pywhatkit.search(command)

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
        # print(ex)
        print('Say it again')
        return "None"
    return result

def execute(command):
    if 'time' in command or 'date' in command or 'weekday' in command:
        dateDetails(command)

    elif 'weather' in command or 'weather update' in command:
        weather()

    # elif "set an alarm" in command:
    #     print("input time example:- 10 and 10 and 10")
    #     talk("Set the time")
    #     a = input("Please tell the time :- ")
    #     alarm(a)
    #     talk("Done,sir")

    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'open' in command or 'go to' in command:
        openBrowser(command)

    elif 'search' in command or 'search in' in command or 'tell me about' in command:
        from search import search
        search()

    elif 'send email' in command:
        openEmail()

    elif 'translate' in command:
        trans()

    elif 'hello' in command or 'hi' in command:
        greet = greeting()
        talk('Hello ' + greet)

    elif command in greetings:
        greetingCheck(command)


    elif 'wikipedia' in command or 'tell me about' in command:
        talk("Searching wikipedia")
        command = command.replace('wikipedia', '')
        result = wikipedia.summary(command, sentences=1)
        print(result)
        talk(result)

    elif 'score' in command:
        from sports import score
        score(command)

    elif 'None' in command:
        print("Error occurred")

    else:
        other(command)

if __name__ == "__main__":
    while True:
        command = take_command()
        if 'wake up' in command:
            from greetings import greeting
            greeting()

            while True:
                command = take_command()
                if 'exit' in command:
                    print("Exiting..")
                    talk("Thank you. Good Bye for now")
                    exit()
                elif 'wake up' in command:
                    talk("I am awake sir. Please tell me, How can I help you ?")
                else:
                    execute(command)
        else:
            print("Please say wake up to start conversation")