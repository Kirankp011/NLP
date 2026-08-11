from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound
import os

text= input("Enter Text:")
target_language = input("Enter target language code(e.g., ml,hi,ja,ta,fr,...):")

try:
    translated_text=GoogleTranslator(
        source="auto",
        target=target_language
    ).translate(text)

    print("Translated Text:", translated_text)

    tts=gTTS(
        text=translated_text,
        lang=target_language
    )
    filename = "translated_audio.mp3"
    tts.save(filename)

    playsound(filename)

    os.remove(filename)
              
except Exception as e:
    print("Error:",e)