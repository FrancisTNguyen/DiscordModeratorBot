import discord
from discord.ext import commands

#this is the token needed to link this bot code back to the discord app
TOKEN = 'NDk5NTAzNTc3MzUwMjc1MDcz.Dp9O5w.TJ09ddv1mW3AqPfym5aLWJlh2eg'
#the prefix before every command this bot takes is '!'. Ex) !online, !offline
client = commands.Bot(command_prefix = '!')

cussWords = ['fuck', 'shit', 'piss', 'dick', 'asshole']
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
    if '!stop' in message.content.lower():
        await client.logout()



#Yushuo will work on the two commands !online & !offline, to prompt the bot
#to go online or offline.  Can add other commands if you want

client.run(TOKEN)
