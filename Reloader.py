import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Reload(commands.Cog):
    
    def __init__(self,client):
        self.client=client

    #reload commands
    @commands.command(name="reload_commands")
    @commands.has_permissions(administrator = True)
    async def UwUcommands_reload(self,message):
        try:
            await self.client.reload_extension("UwUCommands")
        except Exception as e:
            await message.send("Command file did not reload due to this error.")
            await message.send("Error: "+str(e))
            if "TypeError" in str(e):
                await message.send("this is a TypeError error message and it's often cause by not having `self`, please check if you have `self` in your recently added command")
                await message.send("for example: `async def [command_name](self,message)`")
        else:
            await message.send("Command file reloaded")
    @UwUcommands_reload.error
    async def UwUcommands_reload_error(self,message, error):
        if isinstance(error, MissingPermissions):
            await message.send("You do not have permission to run this commmand")

async def setup (client):
    await client.add_cog(Reload(client))