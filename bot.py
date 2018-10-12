import discord
from discord.ext import commands

TOKEN = 'NDk5NTAzNTc3MzUwMjc1MDcz.Dp9O5w.TJ09ddv1mW3AqPfym5aLWJlh2eg'

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_message(message):
    if 'fuck' in message.content:
        await client.send_message(message.channel,'No Cussing!')
    if 'shit' in message.content:
        await client.send_message(message.channel, 'No Cussing!')


@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await client.send_message(channel, '{}: {}'.format(author,content))

client.run(TOKEN)
