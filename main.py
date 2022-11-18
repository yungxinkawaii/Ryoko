import discord
import requests

TOKEN = ""

INSULT_API = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
INSULT_KEY = "insult"
PICK_UP_API = "https://getpickuplines.herokuapp.com/lines/random"
PICK_UP_KEY = "line"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


def get_quote(api_url, key):
    response = requests.get(api_url)
    return response.json()[key]


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
    return

client.run(TOKEN)
