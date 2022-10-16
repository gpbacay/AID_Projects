import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
print(voices[0].name)

engine.say("Hello Sir! I am Jarvis, your personal virtual assistant. How can I help you?")
engine.runAndWait()
engine.stop()

#Run Command: python VoiceTest.py
