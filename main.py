import discord
from discord.utils import get
import os
from datetime import date
import re

from keep_alive import keep_alive

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('&adda'):
        mystring = message.content.split("&adda ", 1)[1]
        mystring = mystring.replace(" ", "-")
        await message.channel.send('https://animixplay.to/v1/' + mystring)
    if message.content.startswith('Waza'):
        await message.channel.send('SUUUUPPP SUUUPPPP!!!!')
    if message.content.startswith('Tilas'):
        await message.channel.send(
            'https://tenor.com/view/belly-dancing-big-tummy-gif-15013188')
    if message.content.startswith('Martim'):
        await message.channel.send('VAI PO CARALHO!')
    if message.content.startswith('test'):
        #print(client.users)
        channel = client.get_channel(693257859194159124)
        #member = client.get_member(188343686084427776)
        user = get(client.get_all_members(), id="188343686084427776")

        #await client.move_to(user, channel)
        mystring = message.content.split("test ", 1)[1]
        mystring = mystring.replace(" ", "-")
        print(mystring)
        # await client.move_to(user, channel)
        a = mystring
        a = a.replace("<", "")
        a = a.replace(">", "")
        a = a.replace("@", "")
        a = a.replace("!", "")
        u = int("188343686084427776")
        print(a)
        print(client.get_user(a))
        #print(client.get_user(mystring))
        print(message.author)
        for x in client.users:
            print(x)
        #await message.author.move_to(channel)
        #await client.move_member(message.author, channel)
        await message.channel.send(message.author.mention)
    if message.content.startswith('123'):
        channel = message.author.voice.channel
        await channel.connect()
        await message.channel.send(
            "!p https://www.youtube.com/watch?v=nZCYrAlfU0E")
    if message.content.startswith('EP'):
        await message.channel.send(
            'https://animixplay.to/anime/40028/Shingeki_no_Kyojin__The_Final_Season'
        )

    if message.content.startswith('Que dia é hoje?'):
        if date.today().weekday() == 6:
            await message.channel.send(file=discord.File('titanfrog.png'))
        else:
            await message.channel.send('Not Aot Sunday...')


keep_alive()
client.run(os.getenv('TOKEN'))
