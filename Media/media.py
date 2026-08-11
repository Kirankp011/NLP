import requests
import pyttsx3
from urllib.parse import quote

engine = pyttsx3.init()

media_name = input("Enter the name of a movie, novel, web series, anime, etc.: ")

try:
    search_url = "https://en.wikipedia.org/w/api.php"

    search_params = {
        "action": "query",
        "list": "search",
        "srsearch": media_name,
        "format": "json"
    }

    search_response = requests.get(
        search_url,
        params=search_params,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    search_data = search_response.json()

    if not search_data["query"]["search"]:
        print("No matching media found.")
        exit()

    title = search_data["query"]["search"][0]["title"]

    summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{quote(title)}"

    summary_response = requests.get(
        summary_url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    summary_data = summary_response.json()

    if "extract" in summary_data:
        synopsis = summary_data["extract"]

        print("\nTitle:", title)
        print("\nSynopsis:\n")
        print(synopsis)

        print("\nReading synopsis aloud...\n")

        engine.say(synopsis)
        engine.runAndWait()

    else:
        print("Synopsis not available.")

except Exception as e:
    print("Error:", e)