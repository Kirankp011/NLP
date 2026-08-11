from ddgs import DDGS 
import requests
from bs4 import BeautifulSoup
import pyttsx3 

engine = pyttsx3.init()

question = input("Enter your Question:")

try:
    with DDGS() as ddgs:
        results = list(ddgs.text(question, max_results=3))

    if not results:
        print("No results found.")
        exit()

    url = results[0]["href"]

    print("Source:", url)

    response = requests.get(
        url,
        headers={"User-Agent":"Mozilla/5.0"},
        timeout=10
    )
    
    soup = BeautifulSoup(response.text, "html.parser")

    paragraphs = soup.find_all("p")

    answer = ""

    for p in paragraphs:
        text = p.get_text(" ", strip=True)
        if len(text) > 100:
            answer = text
            break

    if answer:
        print("\nAnswer:\n")
        print(answer)

        engine.say(answer)
        engine.runAndWait()
    else:
        print("No answer found.")

except Exception as e:
    print("Error:", e)