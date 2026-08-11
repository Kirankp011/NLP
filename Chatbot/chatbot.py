import json
import os 
import pyttsx3

engine = pyttsx3.init()

MEMORY_FILE = "chat_memory.json"

if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as file:
        memory = json.load(file)

else:
    memory = {
        "hi":"Hello!",
        "hello":"Hi there!",
        "good morning":"Good morning!",
        "how are you":"I'm doing well. How are you doing?",
        "what is your name": "I'm Luna, your learning chatbot."
    }

print("Learning Chatbot Started!")
print("Type 'Goodbye' to exit.\n") 

while True:

    user = input("You: ").lower().strip()

    if user == "goodbye":
        print("Luna:Goodbye!")
        engine.say("Goodbye!")
        engine.runAndWait()

        with open(MEMORY_FILE, "w") as file:
            json.dump(memory, file, indent=4)

        break 

    if user in memory:

        reply = memory[user]

        print("Luna:", reply)
        
        engine.say(reply)
        engine.runAndWait()

    else:
        print("Luna: I don't know how to respond to that.")

        engine.say("I dont't know how to respond to that.")
        engine.runAndWait()

        teach = input("Teach me the correct response: ")

        memory[user] = teach

        with open(MEMORY_FILE, "w") as file:
            json.dump(memory, file, indent=4)

        print("Luna: Thank you! I'll remember that.")

        engine.say("Thank you. I'll remember that.")
        engine.runAndWait()  