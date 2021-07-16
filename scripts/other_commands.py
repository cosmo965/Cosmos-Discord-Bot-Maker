# PYTHON 3.9.0
import discord
from discord.ext import commands
import asyncio
import random
import time
import json
import os

# SETTINGS
owner_id = None #editable
currency = None #editable
bot_commands = None #editable
#

intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents,owner_id=owner_id)

usersDir = os.path.join("JSON_FILES", "users.json")

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client
    #START COMMANDS GENERATION HERE
    if (bot_commands["balance"] == True):
        @commands.command(aliases=["bal","bl","currencies"])
        async def balance(self, ctx, member: discord.Member = None):
            async def send(id):
                with open(usersDir, "r") as f:
                    users = json.load(f)
                mAmtString = []
                for i in currency:
                    try:
                        mAmt = users[str(id)][i]
                        mAmtString.append(f"`{str(i)}: {str(mAmt)}` \n")
                    except:
                        print(f"No currency found in the user data. cur: [{i}]")
                        mAmtString.append(f"`{str(i)}: ???` \n")
                balanceEmbeded = discord.Embed(
                    colour=random.randint(0, 0xffffff),
                    title='Balance',
                    description=" ".join(mAmtString)
                )
                await ctx.send(embed=balanceEmbeded)
            if not member:
                await send(ctx.message.author.id)
            else:
                await send(member.id)
    if (bot_commands["simp"] == True):
        @commands.command()
        async def simp(self, ctx, member: discord.Member = None):
            percentSimp = random.randint(1, 100)
            if not member:
                simp0 = discord.Embed(
                    colour=random.randint(0, 0xffffff),
                    title="Simp Count",
                    description=f"{ctx.author.mention} You are {percentSimp}% simp \n"
                    f"Imagine being a simp. I can't relate"
                )
                await ctx.send(embed=simp0)
            else:
                member = member.id
                simp = discord.Embed(
                    colour=random.randint(0, 0xffffff),
                    title="Simp Count",
                    description=f"<@{member}> You are {percentSimp}% simp \n"
                                f"Imagine being a simp. I can't relate"
                )
                await ctx.send(embed=simp)
    
    # CONSTANTS
    if (bot_commands["constant_commands"] == True):
        @commands.command(aliases=["_credits"])
        async def _credentials(self,ctx):
            creditEmbed = discord.Embed(
                colour=random.randint(0, 0xffffff),
                title="Credentials",
                description=f"Front-end programming: Cosmo \n"
                            f"Back-end programming: Cosmo \n"
                            f"Discord bot programming: Cosmo & Bob"
            )
            await ctx.send(embed=creditEmbed)


def setup(client):
    client.add_cog(Commands(client))