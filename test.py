import requests

INSULT_API = "https://insult.mattbas.org/api/insult"

def get_quote():
    response = requests.get(INSULT_API)
    response_text = response.content.decode("utf-8")
    print(response_text)

get_quote()