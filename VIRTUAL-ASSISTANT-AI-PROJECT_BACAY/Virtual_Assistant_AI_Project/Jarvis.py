#Import Libraries
from distutils.cmd import Command
from multiprocessing.connection import wait
from click import CommandCollection
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


#______________________________________________________VOICE_ACTIVATION_COMMAND_FUNCTIONS
#Run Command: python Jarvis.py
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


#______________________________LISTEN_COMMAND_MAIN_FUNCTION
#Run Command: python Jarvis.py
def Listen_command_MainFunction():
    global command
    command = ''
    
    try:
        with sr.Microphone() as source:
            print("Listening...")
            talk("I'm listening")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command


#______________________________ADD_COMMAND_MAIN_FUNCTION
#Run Command: python Jarvis.py
def Add_command_MainFunction(command):
    
    Interrogative_words = ['what', ' what ', 'what ', ' what',
                        'who', ' who ', 'who ', ' who',
                        'where', ' where ', 'where ', ' where',
                        'when', ' when ', 'when ', ' when',
                        'why', ' why ', 'why ', ' why',
                        'how', ' how ', 'how ', ' how']
    try:
        if command in Interrogative_words:
            response = "Would you like to ask me anything else sir?"
            print(response)
            talk(response)
        elif command not in Interrogative_words:
            response = "Is there anything else I could do for you sir?"
            print(response)
            talk(response)
        else:
            response = ''
            print(response)
            talk(response)
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command


#______________________________WAIT_COMMAND_MAIN_FUNCTION
#Run Command: python Jarvis.py
def Wait_command_MainFunction():
    global command
    command = ''
    
    try:
        with sr.Microphone() as source:
            print("Waiting...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command


#_______________________________________________________________________________JARVIS_CORE_FUNCTION
#Run Command: python Jarvis.py
def run_jarvis():
    import os
    import time
    from selenium import webdriver
    
    command = Listen_command_MainFunction()
    

#______________________________________________________________________LISTS_OF_COMMANDS
#Run Command: python Jarvis.py
    Standby_Commands = ["standby",
                        "wait",
                        "wait a sec",
                        "give me a sec",
                        "hold for a sec",
                        "wait for a sec",
                        "give me a second",
                        "hold for a second",
                        "wait for a second",
                        "give me a minute",
                        "hold for a minute",
                        "wait for a minute",
                        "give me an hour",
                        "hold for an hour",
                        "wait for an hour",
                        "just a moment",
                        "just a sec",
                        "just a minute",
                        "just an hour",
                        "call you later",
                        "i'll be back",
                        "be right back"]

    Thankyou_Commands = ["thank you",
                        " thank you ",
                        "thank you ",
                        " thank you",
                        "jarvis thank you",
                        "thank you jarvis",
                        "you've done enough",
                        "that would be all",
                        "thanks",
                        "I said thanks",
                        "I said thank you",
                        "you've done great",
                        "you've done great jarvis"]

    Goodbye_Commands = ["goodbye",
                        " goodbye ",
                        "goodbye ",
                        " goodbye",
                        "good bye",
                        "jarvis goodbye",
                        "goodbye jarvis",
                        "jarvis bye",
                        "bye jarvis",
                        "bye",
                        " bye ",
                        "bye ",
                        " bye",
                        "let's call it a day",
                        "I said goodbye"]

    Stop_Commands = ["jarvis stop",
                    "stop please",
                    "go to sleep",
                    "go to rest",
                    "just go to sleep",
                    "just go to rest",
                    "go to sleep jarvis",
                    "stop listening",
                    "terminate yourself",
                    "enough",
                    "I said enough",
                    "I said stop"]

    No_Commands = ["no",
                    "nah",
                    "none",
                    "none so far",
                    "none at my end",
                    "I'm fine",
                    "I'm good",
                    "this is enough",
                    "I'm good with this",
                    "this is enough",
                    "it is enough",
                    "you've done enough",
                    "I only need this",
                    "not really",
                    "no I don't",
                    "no thanks",
                    "no thank you"
                    "that's a no",
                    "this would suffice",
                    "it would suffice",
                    "I'm not sure",
                    "I'm satisfied",
                    "I said no",
                    "not really",
                    "absolutely not",
                    "absolutely no",
                    "definitely no",
                    "nothing",
                    "nothing at all",
                    "there's nothing",
                    "there's none",
                    "you've done great",
                    "you've done great jarvis"]

    Yes_Commands = ["yes",
                    "yup",
                    "yes please",
                    "of course yes",
                    "yes I do",
                    "I do",
                    "you got it right",
                    "yes actually",
                    "actually yes",
                    "that's a yes",
                    "I think yes",
                    "sure",
                    "yah",
                    "absolutely yes",
                    "definitely yes",
                    "you got it right",
                    "I said yes"]


    Interrogative_words = ["what",
                        " what ",
                        "what ",
                        " what",
                        "who",
                        " who ",
                        "who ",
                        " who",
                        "where",
                        " where ",
                        "where ",
                        " where",
                        "when",
                        " when ",
                        "when ",
                        " when",
                        "why",
                        " why ",
                        "why ",
                        " why",
                        "how",
                        " how ",
                        "how ",
                        " how"]

#_______________________________________________________________________STANDBY_SUBFUNCTION
#Run Command: python Jarvis.py
    def Standby_SubFunction():
        while True:
            command = Wait_command_MainFunction()
            if 'jarvis' in command:
                response = "Yes Sir? How can I help you?"
                talk(response)
                print(response)
                exit(run_jarvis())

#_______________________________________________________________________CONFIRMATION_SUBFUNCTION
#Run Command: python Jarvis.py
    def Confirmation_SubFunction(command):
        
        #if command in Interrogative_words:
            #response = "Would you like to ask me anything else again sir?"
            #talk(response)
        
        command = Add_command_MainFunction(command)
        
        if command in Yes_Commands:
            command = command.replace(command, '')
            response = "Then, what iiss iit?"
            talk(response)
            exit(run_jarvis())
        elif command in No_Commands:
            command = command.replace(command, '')
            response = "Is that so? all right then. Signing off."
            talk(response)
            exit()
        elif '' == command:
            response = "I can't hear anything. Just call me if you need me sir. enjoy yourself."
            talk(response)
            Standby_SubFunction()
        else:
            exit(run_jarvis())


#________________________________________________________________AUTO_REPLACEMENT_SUBFUNCTION
#Run Command: python Jarvis.py
    def Auto_Replacement(command):
    
        try:
            if "what" in command:
                command = command.replace(command, 'what')
            elif "who" in command:
                command = command.replace(command, 'who')
            elif "where" in command:
                command = command.replace(command, 'where')
            elif "when" in command:
                command = command.replace(command, 'when')
            elif "why" in command:
                command = command.replace(command, 'why')
            elif "how" in command:
                command = command.replace(command, 'how')
        except:
            pass
        return command

#________________________________________________________________TERMINATION_STATEMENTS
#Run Command: python Jarvis.py
    if command in Stop_Commands:
        print(command)
        response = "As you wish. signing off."
        print(response)
        talk(response)
        exit()

    elif command in Thankyou_Commands:
        print(command)
        response = "it's my pleasure. signing off."
        print(response)
        talk(response)
        exit()
        
    elif command in Goodbye_Commands:
        print(command)
        response = "Goodbye Sir! enjoy yourself"
        print(response)
        talk(response)
        exit()

#_____________________________________________________________________INTERNET_SEARCH_STATEMENTS
#Run Command: python Jarvis.py
    elif "search" in command:
        response = "Just a moment."
        print(response)
        talk(response)
        information = command.replace("search", '')
        print(information)
        talk("Searching " + information)
        search = command.replace("search", '')
        search = search.replace(' ', '+')
        browser = webdriver.Chrome('chromedriver.exe')
        for i in range(4):
            browser.get("https://www.google.com/search?q=" + search + "&start" + str(i))
        talk("here's what I've found.")
        Confirmation_SubFunction(command)

    elif "play" in command:
        response = "Searching..."
        talk(response)
        song_title = command.replace("play", '')
        pywhatkit.playonyt(song_title)
        response = "Playing " + song_title
        print(response)
        talk(response)
        Confirmation_SubFunction(command)

    elif "who is" in command:
        response = "Searching..."
        print(response)
        talk(response)
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
        Confirmation_SubFunction(command)

#_______________________________________________DATE_and_TIME_STATEMENTS
#Run Command: python Jarvis.py
    elif "date" in command:
        print(command)
        date = datetime.datetime.now().strftime("%m/%d/%y")
        print(date)
        date = date.replace('/', ' ')
        talk("Todays' date is" + date)
        Confirmation_SubFunction(command)

    elif "time" in command:
        print(command)
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        time = time.replace(':', ' ')
        talk("Current time is" + time)
        Confirmation_SubFunction(command) 

#________________________________________________________________________QUERY_STATEMENTS
#Run Command: python Jarvis.py
    elif "who are you" in command:
        command = Auto_Replacement(command)
        response = "Who am I? I am Jarvis, your personal virtual assistant."
        print(response)
        talk(response)
        Confirmation_SubFunction(command)

    elif "who created you" in command:
        command = Auto_Replacement(command)
        print(command)
        response_pronounce = "I am an A.I. or artificial intelligence created by Sir Giiyann Baahcaai. For now, I am only programmed to be his personal virtual assistant."
        response_name = "I am an A.I. or artificial intelligence created by Sir Gianne Bacay. For now, I am only programmed to be his personal virtual assistant."
        print(response_name)
        talk(response_pronounce)
        Confirmation_SubFunction(command)

    elif "what do you think about humans" in command:
        command = Auto_Replacement(command)
        response = "Humans are odd. They think order and chaos are somehow opposites and try to control what won't be. But there is grace in their failings."
        talk(response)
        print(response)
        Confirmation_SubFunction(command) 

#________________________________________________________________________SHUTDOWN_STATEMENTS
#Run Command: python Jarvis.py
    elif "shutdown my computer" in command:
        response = "as you wish! shutting down your computer."
        talk(response)
        print(response)
        os.system("shutdown /s /t 0")
        exit()

    elif "restart my computer" in command:
        response = "as you wish! restarting your computer."
        talk(response)
        print(response)
        os.system("shutdown /r")
        exit()

    elif "sign off my computer" in command:
        response = "as you wish! signing off your computer."
        talk(response)
        print(response)
        os.system("shutdown /l")
        exit()

#________________________________________________________________________STANDBY_STATEMENTS
#Run Command: python Jarvis.py
    elif command in Standby_Commands:
        response = "Understood! Take your time. Just call me if you need anything."
        talk(response)
        print(response)
        Standby_SubFunction()


#_______________________________________________________NoCommands/NotClearCommands_STATEMENTS
#Run Command: python Jarvis.py
    if '' == command:
        print(command)
        response = "I can't hear anything."
        print(response)
        talk(response)
        exit(run_jarvis())

    else:
        print(command)
        response = "Pardon me sir, come again?"
        print(response)
        talk(response)
        exit(run_jarvis())

#______________________________________RUN_JARVIS_IN_A_LOOP_STATEMENT
while True:
    run_jarvis()
#Run Command: python Jarvis.py
