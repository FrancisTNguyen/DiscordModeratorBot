#Danielle Batalla, Francis Nguyen, Yushuo Lu
#CPSC 254-01
#Prof. David Heckathorn

import discord
from discord.ext import commands
import random

#This program creates a Discord 'Bot,' which is built to do the features listed below

#this is the token needed to link this bot code back to the discord app
TOKEN = 'NDk5NTAzNTc3MzUwMjc1MDcz.Dp9O5w.TJ09ddv1mW3AqPfym5aLWJlh2eg'
#the prefix before every command this bot takes is '!'. Ex) !online, !offline
client = commands.Bot(command_prefix = '!')

#use array to store list of curse words to censor
cussWords = ['fuck', 'shit', 'damn', 'bitch', 'crap', 'piss', 'dick', 'cock', 'pussy', 'asshole', 'fag', 'faggot', 'bastard', 'slut', 'douche', 'ass']

#outputs a message saying 'bot is ready' once the program is ready to use
@client.event
async def on_ready():
    print('Bot is ready')

#main event handler.  If a word listed below is detected in the chat
#it would output 'No Cussing' in the chat
@client.event
async def on_message(message):
    #this will convert all text in the message to lower case to handle the case of certain words
    if any(word in message.content.lower() for word in cussWords):
       await client.send_message(message.channel,'No Cussing!')
       await client.delete_message(message)
    await client.process_commands(message)

#command handler.  If a user type '!stop' the program will close
@client.command()
async def stop():
    await client.say('You kids be good now!')
    await client.logout()

#command handler. If a user type '!rollsix' the program will pick a number from 1-6 that is stored in
#a variable called a_number and outputs a number.
@client.command()
async def rollsix():
    a_number = random.randint(1, 6)
    await client.say('You rolled a: ')
    if a_number == 1:
        await client.say(':one:')
    if a_number == 2:
        await client.say(':two:')
    if a_number == 3:
        await client.say(':three:')
    if a_number == 4:
        await client.say(':four:')
    if a_number == 5:
        await client.say(':five:')
    if a_number == 6:
        await client.say(':six:')

#command handler.  If a user types '!coinflip' the program will pick 'heads' or 'tails' from the list 'coin' and outputs one of the options
@client.command()
async def coinflip():
    coin = ['heads', 'tails']
    rand = random.choice(coin)
    await client.say('You got ')
    if rand == 'heads':
        await client.say('heads')
    else:
        await client.say('tails')

#command handler. If a user wants to know the commands of the bot, this program outputs a message saying what the bot does
@client.command()
async def helpme():
    await client.say('Hello! Here are the commands currently available:')
    await client.say('rollsix = Rolls dice')
    await client.say('coinflip = Flips a coin')
    await client.say('join = Joins voice channel')
    await client.say('leave = Leaves voice channel')
    await client.say('yt (insert url) = Plays music')
    await client.say('stop = Stops bot')



client.run(TOKEN)
