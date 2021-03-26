from datetime import date
import riotwatcher
import os
import discord
from discord.ext import commands
import youtube_dl

#authentication on riotwatcher
lol_watcher = riotwatcher.LolWatcher(os.getenv('RIOTT'))
my_region = 'euw1'
##################################################################################################
## Function for the default case
##################################################################################################
async def defaultfunction(message, client):
      return
##################################################################################################
## Function that will choose which type of commands the bot will chose 
##################################################################################################
async def readmessage(message, client):
    switcher = {
        'anime': anime,
    }
    mystring = message.content.split("&", 1)[1]
    checkstring=mystring.split("anime", 1)[0]
    func = switcher.get(checkstring, defaultfunction)
    await func(message, client)

##################################################################################################
## Function that will choose which Lol related function to use with previous symbol
##################################################################################################
async def lol(messagestring,client):
    switcher = {
        'rank': 'exe',
        'perfil': 'exe',
        'winrate': 'exe',
        'champion': 'exe',
        'champ mastey': 'exe',
    }
    func = switcher.get(messagestring[0], defaultfunction)
    await func(messagestring,client)



##################################################################################################
## Function that will chose which function to use with no previous symbol
##################################################################################################
async def random(message,client):
    switcher = {
        'Martim': martim,
        'Tilas': tilas,
        'Waza': waza,
        'Que dia é hoje?': dayis,
        'join': joinvoice,
        'leave': leave
    }
    func = switcher.get(message.content, defaultfunction)
    await func(message,client)    


##################################################################################################
## Function that will choose which Anime related function to use with previous symbol
##################################################################################################
async def anime(message,client):
    switcher = {
        'join':joinvoice,
        'add': 'exe',
        'link': 'exe',
        'day': 'exe',
    }
    mystring = message.content.split("&", 1)[1]
    checkstring=mystring.split("anime", 1)[1]
    func = switcher.get(checkstring, defaultfunction)
    await func(message,client) 


##################################################################################################
## Will send a msg on the previous message channel
##################################################################################################
async def martim(message,client):
  await message.channel.send('VAI PO CARALHO!')


##################################################################################################
## Will send a msg on the previous message channel
##################################################################################################
async def waza(message,client):
  await message.channel.send('SUUUUPPP SUUUPPPP!!!!')



##################################################################################################
## Will send a msg on the previous message channel
##################################################################################################
async def tilas(message,client):
  await message.channel.send(
            'https://tenor.com/view/belly-dancing-big-tummy-gif-15013188')

##################################################################################################
## Will send a msg on the previous message channel
##################################################################################################
async def sasha(message,client):
  await message.channel.send(
            'https://tenor.com/view/belly-dancing-big-tummy-gif-15013188')

##################################################################################################
## Will make bot join voice
##################################################################################################
async def joinvoice(message,client):
    print("cheguei")
    channel = message.author.voice.channel
    await channel.connect()
##################################################################################################
## Will make bot leave  voice
##################################################################################################
async def leave(message,client):
    channel = message.author.voice.channel
    #await channel.disconnect()
    for x in client.voice_clients:
        if(x.channel == client.message.server):
            return await x.disconnect()
    return await client.say("I am not connected to any voice channel on this server!")

##################################################################################################
##################################################################################################
async def test(message, client):
  #print(client.users)
        channel = client.get_channel(693257859194159124)
        #member = client.get_member(188343686084427776)
        # = get(client.get_all_members(), id="188343686084427776")

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



##################################################################################################
##################################################################################################
async def test2(message):
    channel = message.author.voice.channel
    await channel.connect()
    await message.channel.send("!p https://www.youtube.com/watch?v=nZCYrAlfU0E")


##################################################################################################
## Will send a picture in the previous message channel based on the day of the week
##################################################################################################
async def dayis(message,client):
  if date.today().weekday() == 6:
            await message.channel.send(file=discord.File('titanfrog.png'))
  else:
            await message.channel.send('Not Aot Sunday...')

