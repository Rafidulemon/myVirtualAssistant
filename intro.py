from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
import pygame
from pygame import mixer
mixer.init()
import pyttsx3

root = Tk()
root.geometry("500x550")
root.title("Aliza")
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    global img
    img = Image.open("gif.gif")
    lbl = Label(root)
    lbl.place(x=0, y=0)
    i = 0
    for img in ImageSequence.Iterator(img):
        img = img.resize((500, 550))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.05)

play_gif()
talk("Hello Sir. I am Aliza.")
play_gif()
root.mainloop()
