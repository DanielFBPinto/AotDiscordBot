import anime.txt
import discord
import os


def check_anime(message):
 file1 = open('anime.txt', 'r')
 Lines = file1.readlines()
 
 count = 0
 # Strips the newline character
 for line in Lines:
     count += 1
     await message.channel.send("Line{}: {}".format(count, line.strip()))
