import discord
form discord.ext import commands

TOKEN = 'NDk5NTAzNTc3MzUwMjc1MDcz.Dp9O5w.TJ09ddv1mW3AqPfym5aLWJlh2eg
'

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready')

client.run(TOKEN)
