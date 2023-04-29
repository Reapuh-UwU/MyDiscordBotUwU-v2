import discord
import botToken
from discord.ext import commands
from UwUCommands import BotCommand
from Reloader import Reload

TOKEN = botToken.myToken
intents = discord.Intents.all()
client = commands.Bot(command_prefix = "!",case_insensitive=True,intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    await client.load_extension("UwUCommands")
    await client.load_extension("Reloader")

client.run(TOKEN)