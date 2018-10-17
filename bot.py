import discord
from discord.ext import commands

#this is the token needed to link this bot code back to the discord app
TOKEN = 'NDk5NTAzNTc3MzUwMjc1MDcz.Dp9O5w.TJ09ddv1mW3AqPfym5aLWJlh2eg'
#the prefix before every command this bot takes is '!'. Ex) !online, !offline
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready')

#main event handler.  If a word listed below is detected in the chat
#it would output 'No Cussing' in the chat
@client.event
async def on_message(message):
    if 'fuck' in message.content.lower():
        await client.send_message(message.channel,'No Cussing!')
    if 'shit' in message.content.lower():
        await client.send_message(message.channel, 'No Cussing!')
    if 'bitch' in message.content.lower():
        await client.send_message(message.channel, 'No Cussing!')
    if 'ass' in message.content.lower():
        await client.send_message(message.channel, 'No Cussing!')
    if 'crap' in message.content.lower():
        await client.send_message(message.channel, 'No Cussing!')
    if 'piss' in message.content.lower():
        await client.send_message(message.channel, 'No Cussing!')
    if 'douche' in message.content.lower():
        await client.send_message(message.channel, 'No Cussing!')
    if 'dick' in message.content.lower():
        await client.send_message(message.channel, 'No Cussing!')
#another event handler.  If a user deletes a message,the bot will output
#the deleted message and the user that deleted it
@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await client.send_message(channel, '{}: {}'.format(author,content))

#Yushuo will work on the two commands !online & !offline, to prompt the bot
#to go online or offline.  Can add other commands if you want

client.run(TOKEN)
