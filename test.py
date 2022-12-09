import requests
import json

INSULT_API = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
INSULT_KEY = "insult"
PICK_UP_API = "https://api.jcwyt.com/pickup?type=json"
PICK_UP_KEY = "line"


def get_quote(api_url, key):
    response = requests.get(api_url)
    # response_text = json.load(response.json())
    response.json()
    respond = str(response.content, 'UTF-8')
    print(respond)
    print(response)
    print(type(response))


get_quote(PICK_UP_API, PICK_UP_KEY)
