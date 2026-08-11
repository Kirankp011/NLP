import pyttsx3

engine = pyttsx3.init()

text = input("Enter text in English:")

engine.say(text)
engine.runAndWait()