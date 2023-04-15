import discord
import botToken
from discord.ext import commands
from UwUCommands import BotCommand

TOKEN = botToken.myToken
intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!',case_insensitive=True,intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.load_extension('UwUCommands')

#reload command
@client.command()
async def reload(message):
    try:
        await client.reload_extension('UwUCommands')
    except Exception as e:
        await message.send("reload is not complete")
        await message.send("Error:"+str(e))
    else:
        await message.send("reload complete")

#ping
@client.command()
async def ping(message):
    await message.send(f'HA! GET PONGED!! bot latency is {round(client.latency * 1000)}ms')
client.run(TOKEN)