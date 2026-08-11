from googletrans import Translator

translator = Translator()

text = input("Enter your text in English:")

translated = translator.translate(text, dest='ml')
print("Malayalam:", translated.text)