import wikipedia
import webbrowser
import pyttsx3
import googletrans
import speech_recognition as sr
import pywhatkit

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

def google(query):
    import wikipedia as googleScrap
    query = query.replace("jarvis", "")
    query = query.replace("google search", "")
    query = query.replace("google", "")
    talk("This is what I found on google")

    try:
        talk("Seaching "+ query)
        pywhatkit.search(query)
        result = googleScrap.summary(query, 1)
        talk(result)

    except:
        talk("No speakable output available")

def youtube(query):

    talk("This is what I found for your search!")
    query = query.replace("youtube search", "")
    query = query.replace("youtube", "")
    query = query.replace("aliza", "")
    web  = "https://www.youtube.com/results?search_query=" + query
    webbrowser.open(web)
    pywhatkit.playonyt(query)
    talk("Done, Sir")


def search():
    talk("Can you tell me where should I search ?")
    command = take_command()

    if 'google' in command:
        talk("What should I search Sir?")
        command = take_command()
        google(command)
    elif 'youtube' in command:
        talk("What should I search Sir?")
        command = take_command()
        youtube(command)
    else:
        talk("What should I search Sir?")
        command = take_command()
        pywhatkit.search(command)