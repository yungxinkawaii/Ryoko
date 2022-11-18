import requests
import json

INSULT_API = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
INSULT_KEY = "insult"
PICK_UP_API = "https://getpickuplines.herokuapp.com/lines/random"
PICK_UP_KEY = "line"


def get_quote(api_url, key):
    response = requests.get(api_url)
    # response_text = json.load(response.json())
    respond = response.json()[key]
    print(respond)
    print(type(respond))


get_quote(PICK_UP_API, PICK_UP_KEY)
