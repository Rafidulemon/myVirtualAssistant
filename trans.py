import speech_recognition as sr
import pyttsx3
import os
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