#Import Libraries
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

#Declare Variables
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

#Voice Activation
engine.setProperty('voice', voices[2].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            talk('Im listening')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'thenied' in command:
                command = command.replace('thenied', '')
                print(command)
    except:
        pass
    return command

#Input Commands
def run_thenied():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'Who created you?' in command:
        talk('Gianne Bacay was my creator')
    elif 'tell me a joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('pardon me, please say the command again.')

#While Loop
while True:
    run_thenied()

#Run Command: python TheNied.py
