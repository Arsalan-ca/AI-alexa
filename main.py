import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
situations = True
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():

    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alex' in command:
                command = command.replace('alex', '')
                print(command)

    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
        situations = False
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is' + time)
    elif 'who is the' in command:
        person = command.replace('whi is the', '')
        info = wikipedia.summary(person, 1)  ##number is for how manny line do you want
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have headache')
    elif 'are you single' in command:
        talk("I'm in relationship with Juli")
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'open chrome' in command:
        subprocess.call("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        #import os
        #os.startfile('C:\\myprogram.exe')
    else:
        talk('Please say that command again')


while situations:
    run_alexa()
