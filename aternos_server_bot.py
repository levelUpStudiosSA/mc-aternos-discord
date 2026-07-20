import discord
import os
from python_aternos import Client
import time
import asyncio

TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

aternos = Client.from_credentials('discord1bot', 'MTUyODc5NjQ3Njg2MjM3MDA4Mw.G4q7qc.uEOV4v09JCtZYEWBd61CpR2uEbDUboHUeKCBIY')
atservers = aternos.list_servers()
myserv = atservers[0]

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = message.author.name 
    user_message = str(message.content)
    
    if isinstance(message.channel, discord.TextChannel):
        channel = message.channel.name
    else:
        channel = "DM"
        
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if channel == 'bot-cmnds':
        if user_message.lower() == '?hello':
            await message.channel.send(f'Hello {username}!')
            return

        if user_message.lower() == '?server_start':
            myserv.start()
            while True:
                ping = str(os.popen('mcstatus OGZsmp.aternos.me status | grep description').read())
                if "offline" in ping:
                    await asyncio.sleep(1)
                else:
                    break
            await message.channel.send("server is now alive!!! you can join in 2-3 minutes by pasting ||OGZsmp.aternos.me:50529|| in the server address.")
            return

        if user_message.lower() == '?server_stop':
            myserv.stop()
            await message.channel.send('server stopped')
            return

client.run(TOKEN)
