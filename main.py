import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import googletrans
import playsound
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from AssistantUI import Ui_MainWindow
import sys


r = sr.Recognizer()
translator = googletrans.Translator()
translate_to = 'ja'
greetings = ['good morning', 'good afternoon', 'good evening', 'good night']
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

def execute(command):
    if 'time' in command or 'date' in command or 'weekday' in command:
        from dateTime import dateDetails
        dateDetails(command)

    elif 'weather' in command or 'weather update' in command:
        from weather import weather
        weather()

    elif 'temperature' in command:
        from temperature import Temperature
        Temperature()

    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'open' in command or 'go to' in command:
        from open import openBrowser
        openBrowser(command)

    elif 'search' in command or 'search in' in command or 'tell me about' in command:
        from search import search
        search()

    elif 'world cup points table' in command:
        from sports import fixture
        fixture()

    elif 'world cup live' in command:
        from sports import fifaLive
        fifaLive()

    elif 'send email' in command:
        from open import openEmail
        openEmail()

    elif 'translate' in command:
        from trans import trans
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
        from otherCommands import other
        other(command)

def TaskExe():
    if __name__ == "__main__":
        # from FaceRecognition import rec
        # rec()
        while True:
            command = take_command()
            if 'alisha' in command or 'aliza' in command or 'alija' in command or 'alesha' in command\
                    or 'aleza' in command or 'aleja' in command or 'lisa' in command\
                    or 'eliza' in command or 'aligarh' in command or 'alyssa' in command:
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
                talk("Sorry! Unauthorized command detected. I can not move forward without authorized command")
                print("Unable to start")


#GUI code here
class MainThread(QThread):

    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.Task_Gui()

    def Task_Gui(self):

        TaskExe()


startFunctions = MainThread()


class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()

        self.jarvis_ui = Ui_MainWindow()

        self.jarvis_ui.setupUi(self)

        self.jarvis_ui.pushButton.clicked.connect(self.startFunc)

        self.jarvis_ui.pushButton_2.clicked.connect(self.close)


    def startFunc(self):
        self.jarvis_ui.movies = QtGui.QMovie("gif.gif")

        self.jarvis_ui.Gif.setMovie(self.jarvis_ui.movies)

        self.jarvis_ui.movies.start()

        self.jarvis_ui.movies_2 = QtGui.QMovie("gif3.gif")

        self.jarvis_ui.Gif_2.setMovie(self.jarvis_ui.movies_2)

        self.jarvis_ui.movies_2.start()

        self.jarvis_ui.movies_3 = QtGui.QMovie(
            "gif4.gif")

        self.jarvis_ui.Gif_3.setMovie(self.jarvis_ui.movies_3)

        self.jarvis_ui.movies_3.start()

        self.jarvis_ui.movies_4 = QtGui.QMovie("gif5.gif")

        self.jarvis_ui.Gif_4.setMovie(self.jarvis_ui.movies_4)


        self.jarvis_ui.movies_4.start()


        timer = QTimer(self)

        timer.timeout.connect(self.showtime)

        timer.start(1000)

        self.showDate()
        self.showWeek()

        startFunctions.start()

    def showtime(self):
        current_time = QTime.currentTime()

        label_time = current_time.toString("hh:mm:ss")

        labbel = "Time:" + label_time

        self.jarvis_ui.textBrowser.setText(labbel)

    def showDate(self):
        current_date = QDate.currentDate()
        label_date = current_date.toString("dd-MMMM yyyy")
        labbbel = label_date
        self.jarvis_ui.textBrowser_2.setText(labbbel)

    def showWeek(self):
        current_date = QDate.currentDate()
        label_date = current_date.toString("dddd")
        labbbel = label_date
        self.jarvis_ui.textBrowser_7.setText(labbbel)

Gui_App = QApplication(sys.argv)

Gui_Jarvis = Gui_Start()

Gui_Jarvis.show()

exit(Gui_App.exec_())
