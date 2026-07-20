import discord
import os
from python_aternos import Client
import asyncio

TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

ATERNOS_COOKIE = "WW5uvr7D7dmD8Me40YQEUfEgOv94b7hKKIpyrk9SeDYnnYb6wRFQJ6FmjwpaRmtpMmVnhA25eqmJ82JxkLwAJ9PFf0PRbV9g7nnn"

aternos = Client.from_cookie(ATERNOS_COOKIE)
atservers = aternos.list_servers()
myserv = atservers[0]

@client.event
async def on_ready():
    print('Bot is ready!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if isinstance(message.channel, discord.TextChannel) and message.channel.name == 'bot-cmnds':
        if message.content.lower() == '?hello':
            await message.channel.send(f'Hello {message.author.name}!')
        
        elif message.content.lower() == '?server_start':
            myserv.start()
            while True:
                ping = str(os.popen('mcstatus OGZsmp.aternos.me status | grep description').read())
                if "offline" in ping:
                    await asyncio.sleep(1)
                else:
                    break
            await message.channel.send("Server is starting! Join in 2-3 mins: OGZsmp.aternos.me:50529")
            
        elif message.content.lower() == '?server_stop':
            myserv.stop()
            await message.channel.send('Server stopped')

client.run(TOKEN)
