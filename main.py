import discord
import asyncio
import random
import string

token = 'Token Here'
client = discord.Client()

@client.event
async def on_ready():
    print ('Logged in as')
    print (client.user.name)
    print (client.user.id)
    print ('Ready to start spam.')
    print ('--------------------')

@client.event
async def on_message(message):
    if message.content.startswith(".s") and message.author == client.user:
        await client.delete_message(message)
        for x in range(50):
            asc = ""
            for x in range(1999):
                num = random.randrange(13000)
                asc = asc + chr(num)
            await client.send_message(message.channel, asc)


client.run(token, bot=False)
