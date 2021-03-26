import discord
from discord.utils import get
import asyncio
import os
import functions
from datetime import date
from keep_alive import keep_alive


client = discord.Client()

#Bot loggs in to discord
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))




#catches an event, if it's from the bot itself, ignore else checks if it has content that the bot recognizes
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('&'):
       await functions.readmessage(message,client)
    else:
      #await message.channel.send('VAI PO CARALHO!')
      await functions.random(message,client)
   

   

#keeps the bot alive with a ping every five minutes
keep_alive()

#Authentication on discord
client.run(os.getenv('TOKEN'))

