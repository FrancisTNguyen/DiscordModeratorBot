import discord
from discord.ext import commands
import random

#this is the token needed to link this bot code back to the discord app
TOKEN = 'NDk5NTAzNTc3MzUwMjc1MDcz.Dp9O5w.TJ09ddv1mW3AqPfym5aLWJlh2eg'
#the prefix before every command this bot takes is '!'. Ex) !online, !offline
client = commands.Bot(command_prefix = '!')

cussWords = ['fuck', 'shit', 'damn', 'bitch', 'crap', 'piss', 'dick', 'cock', 'pussy', 'asshole', 'fag', 'faggot', 'bastard', 'slut', 'douche', 'ass']
@client.event
async def on_ready():
    print('Bot is ready')

#main event handler.  If a word listed below is detected in the chat
#it would output 'No Cussing' in the chat
@client.event
async def on_message(message):
    if any(word in message.content.lower() for word in cussWords):
       await client.send_message(message.channel,'No Cussing!')
       await client.delete_message(message)
    await client.process_commands(message)
    #if '!stop' in message.content.lower():
        #await client.logout()

@client.command()
async def stop():
    await client.say('You kids be good now!')
    await client.logout()

@client.command()
async def rollsix():
    a_number = random.randint(1, 6)
    await client.say('You rolled a: ')
    await client.say(a_number)

@client.command()
async def coinflip():
    coin = ['heads', 'tails']
    rand = random.choice(coin)
    await client.say('You got ')
    await client.say(rand)

client.run(TOKEN)
