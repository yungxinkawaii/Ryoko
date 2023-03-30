import discord
import requests
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')

# TOKEN = "MTA0MzE1OTk2NjQ5MzcyNDY4Mw.GHWJjX.ZQ9zoANwUtpNF_kYSGp2Q86C_2IcSLUu90-HTw"

INSULT_API = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
INSULT_KEY = "insult"
PICK_UP_API = "https://api.jcwyt.com/pickup?type=json"
PICK_UP_KEY = "line"
BIRYANI_API = "https://biriyani.anoram.com/get"
BIRYANI_KEY = "image"
CAT_API = "https://api.thecatapi.com/v1/images/search"
CAT_KEY = "url"
CAT_API_KEY = os.getenv('CAT_API_KEY')

cat_string_list = ["sad", "upset", "angry", "mad", "depressed", "lonely",
                   "crying", "cry", "tired", "cat", "cute", "kitty", "kitten", "meow"]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


def get_quote(api_url, key, api_key=None):
    if api_key:
        # Set the request headers to include the API key
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        # Make the API request
        response = requests.get(api_url, headers=headers)
    else:
        response = requests.get(api_url)

    try:
        if isinstance(response.json(), list):
            return response.json()[0][key]
        else:
            return response.json()[key]
    except Exception:
        return str(response.content, 'UTF-8')


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hi'):
        await message.channel.send('Yo simp.')
    elif message.content.startswith('$bye'):
        await message.channel.send('Get lost.')
    elif message.content.startswith('$insult'):
        await message.channel.send(get_quote(INSULT_API, INSULT_KEY))
    elif message.content.startswith('$flirt'):
        await message.channel.send(get_quote(PICK_UP_API, PICK_UP_KEY))
    elif "biryani" in message.content.lower():
        await message.channel.send(get_quote(BIRYANI_API, BIRYANI_KEY))
    elif any(s in message.content.lower() for s in cat_string_list):
        await message.channel.send(get_quote(CAT_API, CAT_KEY, CAT_API_KEY))
        await message.channel.send("Here's a cat for you :3")
    return

client.run(TOKEN)
