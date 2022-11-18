import discord
import requests

TOKEN = "MTA0MzE1OTk2NjQ5MzcyNDY4Mw.Gu5FZ7.YFsn_dNwXn067FjMCwdPQq2UOqZwIpZ0_VG-9Q"
INSULT_API = "https://insult.mattbas.org/api/insult"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


def get_insult_quote():
    response = requests.get(INSULT_API)
    return response.content.decode("utf-8")


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
    elif message.content.startswith('$insult me'):
        await message.channel.send(get_insult_quote())
    return

client.run(TOKEN)
