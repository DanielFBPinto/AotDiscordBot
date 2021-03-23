from datetime import date
import riotwatcher
import os

#authentication on riotwatcher
lol_watcher = riotwatcher.LolWatcher(os.getenv('RIOTT'))
my_region = 'euw1'

##################################################################################################
## Function that will choose which type of commands the bot will chose 
##################################################################################################
def readmessage(message, client):
    switcher = {
        '': 'exe',
    }
    func = switcher.get(message[0], lambda: "Invalid function")
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
    func = switcher.get(messagestring[0], lambda: "Invalid function")
    await func(messagestring,client)



##################################################################################################
## Function that will chose which function to use with no previous symbol
##################################################################################################
async def random(message):
    switcher = {
        'Martim': martim,
        'Tilas': tilas,
        'Waza': waza,
        'Que dia é hoje': 'dayis' 
    }
    func = switcher.get(message.content, lambda: "Invalid function")
    await func(message)    


##################################################################################################
## Function that will choose which Anime related function to use with previous symbol
##################################################################################################
def anime(messagestring):
    switcher = {
        'add': 'exe',
        'link': 'exe',
        'day': 'exe',
    }
    func = switcher.get(messagestring[0], lambda: "Invalid function")
    func() 


##################################################################################################
## Will send a msg on the previous message channel
##################################################################################################
async def martim(message):
  await message.channel.send('VAI PO CARALHO!')


##################################################################################################
## Will send a msg on the previous message channel
##################################################################################################
async def waza(message):
  await message.channel.send('SUUUUPPP SUUUPPPP!!!!')



##################################################################################################
## Will send a msg on the previous message channel
##################################################################################################
async def tilas(message):
  await message.channel.send(
            'https://tenor.com/view/belly-dancing-big-tummy-gif-15013188')




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
async def dayis(message, discord):
  if date.today().weekday() == 6:
            await message.channel.send(file=discord.File('titanfrog.png'))
  else:
            await message.channel.send('Not Aot Sunday...')

