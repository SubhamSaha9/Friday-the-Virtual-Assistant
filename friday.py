import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import ctypes
import os
from ecapture import ecapture as ec

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voice_index = 1
engine.setProperty('voice', voices[voice_index].id)
newVoiceRate = 145
engine.setProperty('rate', newVoiceRate)


engine.say('hi! Friday this side')
engine.say('what can i do for you')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'friday' in command:
                command = command.replace('friday ', '')
                # talk(command)
    except:
        pass
    return command


def run_friday():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        talk('current time is '+time)
    elif 'open' in command:
        if 'instagram' in command:
            talk('opening instagram')
            webbrowser.open('https: // www.instagram.com/')
        elif 'facebook' in command:
            talk('opening facebook')
            webbrowser.open('https://www.facebook.com/')
        elif 'twitter' in command:
            talk('opening twitter')
            webbrowser.open('https://www.twitter.com/')
        elif 'linledln' in command:
            talk('opening linkedln')
            webbrowser.open('https://www.linledln.com/')
        elif 'youtube' in command:
            talk('opening youtube')
            webbrowser.open('https://www.youtube.com/')
        else:
            query = command.replace("open ", "")
            talk('opening '+query)
            webbrowser.open('https://www.'+query+'.com/')
    elif 'search' in command:
        query = command.replace("search", "")
        talk('showing results for '+query)
        webbrowser.open('https://www.google.com/search?q='+query)
    elif "who are you" in command:
        talk("I am your virtual assistant Friday, created by Subham")
    elif 'lock screen' in command:
        talk("locking the device")
        ctypes.windll.user32.LockWorkStation()
    elif 'shutdown system' in command:
        talk("Hold On a Sec ! Your system is on its way to shut down")
        os.system("shutdown /s /t 30")
    elif 'restart system' in command:
        talk("Hold On a Sec ! Your system is on its way to restart")
        os.system("shutdown /r /t 30")
    elif "camera" in command or "take a photo" in command:
        talk('hold on taking picture')
        ec.capture(0, "Friday Camera ", "img.jpg")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif "where is" in command:
        query = command.replace("where is ", "")
        location = query
        talk("User asked to Locate"+location)
        talk('here are some results')
        webbrowser.open(
            "https://www.google.com/maps/search/" + location)
    elif "who is" in command or "what is" in command:
        if "who is" in command:
            question = command.replace("who is", "")
        else:
            question = command.replace("what is", "")

        info = wikipedia.summary(question, 1)
        print(info)
        talk(info)
    elif "do you love me" in command:
        talk("Sorry but I am already committed with wifi")
    else:
        talk("please say that again.")


while True:
    run_friday()
