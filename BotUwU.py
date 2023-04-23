import discord
import botToken
from discord.ext import commands
from UwUCommands import BotCommand
from discord.ext.commands import has_permissions, MissingPermissions

TOKEN = botToken.myToken
intents = discord.Intents.all()
client = commands.Bot(command_prefix = "!",case_insensitive=True,intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    await client.load_extension("UwUCommands")

#reload command
@client.command(name="reload_commands")
@commands.has_permissions(administrator = True)
async def UwUcommands_reload(message):
    try:
        await client.reload_extension("UwUCommands")
    except Exception as e:
        await message.send("Command file did not reload due to this error.")
        await message.send("Error: "+str(e))
        if "TypeError" in str(e):
            await message.send("this is a TypeError error message and it's often cause by not having `self`, please check if you have `self` in your recently added command")
            await message.send("for example: `async def [command_name](self,message)`")
    else:
        await message.send("Command file reloaded")
@UwUcommands_reload.error
async def UwUcommands_reload_error(message, error):
    if isinstance(error, MissingPermissions):
        await message.send("You do not have permission to run this commmand")

#ping
@client.command()
async def ping(message):
    await message.send(f"HA! GET PONGED!! bot latency is {round(client.latency * 1000)}ms")



client.run(TOKEN)