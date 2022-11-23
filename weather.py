from tkinter import *
import requests
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 190)

def talk(text):
    engine.say(text)
    engine.runAndWait()
def search():
    pass

app = Tk()
app.title("Weather update")
app.geometry('700x350')

def weather():
    city_text = StringVar()
    city_entry = Entry(app, textvariable=city_text)
    city_entry.pack()

    search_btn = Button(app, text='Search wearther', width=12, command=search)
    search_btn.pack()

    location_lbl = Label(app, text='Location', font=('bold', 20))
    location_lbl.pack()

    image =Label(app, bitmap='')
    image.pack()

    temp_lbl = Label(app, text='Temperature')
    temp_lbl.pack()

    weather_lbl = Label(app, text='Weather')
    weather_lbl.pack()


weather()
app.mainloop()