from urllib import response
from discord.ext import commands
import discord
import random
import requests
import uwuify



class BotCommand(commands.Cog):

    def __init__(self,client):
        self.client=client

    #embed/help zone
    @commands.command(aliases=["commands"])
    async def help(self,message):
        embed = discord.Embed(
            title="commands?",
            description="This is the help section. Here are all the commands for me!", #continue me
            colour=discord.Colour(0xd88c54)
            )
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/944013283327893545/d15911188dda36091a1fc1813ef4263f.webp?size=2048")
        embed.add_field(
            name="!help",
            value="List all of the commands",
            inline=False
        )
        embed.add_field(
            name="!hello",
            value="Hello to the user",
            inline=False
        )
        embed.add_field(
            name="!rng",
            value="Gives a random number with the given range that is given by the user. Example !rng 0 10",
            inline=False
        )
        embed.add_field(
            name="!ping",
            value="HA GET PONGED. I think you know this command is...",
            inline=False
        )
        embed.add_field(
            name="!mcstatus",
            value="Gives the hostname, status, ip, max and current player count",
            inline=False
        )
        embed.add_field(
            name="!xkcd",
            value="Sends a xkcd comic within a given number. Example: !xkcd 5",
            inline=False
        )
        embed.add_field(
            name="!rngxkcd",
            value="Sends a random xkcd comic",
            inline=False
        )
        embed.add_field(
            name="!tomfoolery",
            value="run the command and find out",
            inline=False
        )
        await message.send(embed=embed)

    #message commands/FUN COMMANDS!#
    @commands.command()
    async def hello(self,message):
        await message.send(f"Hello {message.author.mention}!")

    @commands.command()
    async def neat(self,message):
        await message.send("neat")
        
    @commands.command(aliases=["numbergen"])
    async def rng(self,message,number1,number2):
        number1 = (int(number1))
        number2 = (int(number2))
        result = random.randrange(number1,number2)
        response = (f"This is your random number: **``{result}``**!")
        await message.send(response)
        
    #MCstats#
    @commands.command(aliases=["serverstatus"])
    async def mcstatus(self,message,IP):
        response = requests.get(f"https://api.mcsrvstat.us/2/{IP}")
        status = response.json()
        if status["online"] == True:
            x = "Online"
            #turning things to string UwU
            player_online=str(status["players"]["online"])
            player_max=str(status["players"]["max"])
            player_ratio=player_online + "/" + player_max

            #player check
            embed = discord.Embed(
                title="Minecraft server",
                colour=discord.Colour(0xd88c54)
            )
            embed.add_field(
                name="Minecraft Server IP",
                value=IP,
                inline=False
            )

            embed.add_field(
                name="Server version",
                value=status["version"],
                inline=False
                )
            embed.add_field(
                name="Status",
                value=x,
                inline=False
            )

            if "list" in status["players"]:
                embed.add_field(
                    name="Player list",
                    value=status["players"]["list"],
                    inline=False
                )
            embed.add_field(
                name="Player count",
                value=player_ratio,
                inline=False
            )

            if "software" in status:
                embed.add_field(
                    name="Sofrware version",
                    value=status["software"],
                    inline=False
                    )
                
            await message.send(embed=embed)
        else:
            x = "Offline"
            await message.send("The server your trying to check is unavailable. Please check if the type the correct server address/ip and its online.")
    
    #XKCD SECTIONS#
    @commands.command()
    async def xkcd(self,message,number):
        #xkcd checker
        checker = requests.get("https://xkcd.com/info.0.json")
        status_checker = checker.json()
        limit = status_checker["num"]
        if int(number) <= int(limit) and int(number) > 0:
            response = requests.get(f"https://xkcd.com/{number}/info.0.json")
            status = response.json()
            await message.send(status["img"])
        else:
            await message.send(f"the number you typed is not not available. Make sure the number is between 1 to {limit}.")

    @commands.command()
    async def rngxkcd(self,message):
        #xkcd checker
        checker = requests.get("https://xkcd.com/info.0.json")
        status_checker = checker.json()
        limit = status_checker["num"]
        rng = random.randrange(1,limit)
        response = requests.get(f"https://xkcd.com/{rng}/info.0.json")
        status = response.json()
        await message.send(status["img"])

    #we do alittle bit of trolling
    @commands.command(aliases=["troll"])
    async def tomfoolery(self,message):
        await message.send("@everyone")
        await message.send("@here")
        await message.send({message.author.mention})

    #ping
    @commands.command(aliases=["pong"])
    async def ping(self,message):
        await message.send(f"HA! GET PONGED!! bot latency is {round(self.client.latency * 1000)}ms")

    #UwU Translator Section
    @commands.command(aliases=["uwu", "uwuinator"])
    async def uwufy(self,message,*,ctx):
        await message.send(uwuify.uwu(ctx))

    @commands.command(aliases=["chickenbutt"])
    async def guesswhat(self,message):
        await message.send(f"chickenbutt")

async def setup (client):
    await client.add_cog(BotCommand(client))