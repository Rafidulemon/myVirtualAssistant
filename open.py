import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import smtplib
import subprocess
import calendar

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

    elif 'messenger' in command:
        from messenger import messenger
        messenger()

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
    elif 'live tv' in command or 'tv' in command or 'tb' in command:
        talk("Opening live TV Sir")
        webbrowser.open("http://tv.ebox.live/")
    elif 'vs code' in command:
        talk("Opening visual studio for you")
        path = "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path)

    elif 'task manager' in command:
        talk("Opening task manager sir")
        # path = "%windir%\\system32\\taskmgr.exe /7"
        # os.startfile(path)
        os.system('taskmgr')

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

    elif 'microsoft' in command:
        microsoft(command)

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
    server.login('rafid.nexkraft@gmail.com', 'rafid000')
    server.sendmail('rafid.nexkraft@gmail.com', to, content)
    server.close()

def microsoft(command):
    if 'word' in command:
        talk("Opening Microsoft word sir")
        path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
        os.startfile(path)

    elif 'powerpoint' in command:
        talk("Opening Microsoft powerpoint sir")
        path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
        os.startfile(path)

    elif 'excel' in command:
        talk("Opening Microsoft excel sir")
        path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
        os.startfile(path)

    else:
        talk("Command not found")
        print("Command not found")