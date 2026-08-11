import speech_recognition as sr 
from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound
import os

target_language=input("Enter target language code:")

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak now.....")

    recognizer.adjust_for_ambient_noise(source)

    try:
        audio = recognizer.listen(source,timeout=5)

        text = recognizer.recognize_google(audio)

        print("you said:", text)

        translated_text = GoogleTranslator(
            source='auto',
            target=target_language
        ).translate(text)

        print("Translated:",translated_text)

        tts=gTTS(
            text=translated_text,
            lang=target_language
        )

        filename="translated.mp3"
        tts.save(filename)

        playsound(filename)

        os.remove(filename)

    except sr.WaitTimeoutError:
        print("No speech detected.")

    except sr.UnknownValueError:
        print("Could not understand speech.")

    except Exception as e:
        print("Error:", e)