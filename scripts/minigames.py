# PYTHON 3.9.0
import discord
from discord.ext import commands
import asyncio
import random
import time
import json
import os

'''
rps = {'bool': True, 'cooldown': 0, 'currencies': {}, 'other_args': {'messages': ['Yes', 'ntf', 'fgtf']}}
coinFlip = {'bool': False, 'cooldown': 0, 'currencies': {}, 'other_args': {}}
owner_id = ['ffds']
'''
# SETTINGS
rps = None #editable
coinFlip = None #editable
owner_id = None #editable
#

intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents,owner_id=owner_id)

usersDir = os.path.join("JSON_FILES", "users.json")

class Minigames(commands.Cog):
    def __init__(self, client):
        self.client = client
    if rps['bool'] == True:
        @commands.command(aliases=["rockpaperscissors"])
        @commands.cooldown(1, rps["cooldown"], commands.BucketType.user)
        async def rps(self, ctx):
            async def give_money(user,currency,amount):
                with open(usersDir) as f:
                    users = json.load(f)
                users[f"{user.id}"][currency] += amount
                with open(usersDir, "w") as f:
                    json.dump(users, f, indent=4)
            randomMoney = None

            choices = ["rock", "paper", "scissors"]
            botChoice = random.choice(choices)

            async def sendLoseEmbeded(mAmt):
                mAmtString = []
                for i in mAmt:
                    mAmtString.append(f"`{str(i)}: {str(mAmt[i])}` \n")
                loseEmbeded = discord.Embed(
                    colour=discord.Color.red(),
                    title='**YOU LOST RPS**',
                    description=f"{rps['other_args']['messages'][1]} \n The bot chose `{botChoice}` \n You lost:\n {' '.join(mAmtString)}"
                )
                await ctx.send(embed=loseEmbeded)
            async def sendTieEmbeded():
                tieEmbeded = discord.Embed(
                    colour=discord.Color.orange(),
                    title='**TIE**',
                    description=
                                f"{rps['other_args']['messages'][2]} \n"
                                f"The bot chose `{botChoice}` \n"
                                f"You earned nothing"
                )
                await ctx.send(embed=tieEmbeded)
            async def sendWinEmbeded(mAmt):
                mAmtString = []
                for i in mAmt:
                    mAmtString.append(f"`{str(i)}: {str(mAmt[i])}` \n")
                winEmbeded = discord.Embed(
                    colour=discord.Color.green(),
                    title='**YOU WON RPS**',
                    description=f"{rps['other_args']['messages'][0]} \n The bot chose `{botChoice}` \n You win:\n {' '.join(mAmtString)}"
                )
                await ctx.send(embed=winEmbeded)
            
            try:
                await ctx.send("Please choose between `rock`, `paper`, or `scissors`")
                playerMessage = await self.client.wait_for(
                    "message",
                    timeout=30,
                    check=lambda m: m.author == ctx.author and m.channel == ctx.channel
                )
                if playerMessage:
                    if playerMessage.content.lower() == "scissors":
                        if botChoice == "rock":
                            yes = {}
                            for cur_currency in rps["currencies"]:
                                maximum = rps["currencies"][cur_currency][0]
                                minimum = rps["currencies"][cur_currency][1]
                                randomMoney = random.randint(maximum,minimum)
                                yes[cur_currency] = -randomMoney
                                await give_money(ctx.author,cur_currency,-randomMoney)
                            await sendLoseEmbeded(yes)
                        elif botChoice == "scissors":
                            await sendTieEmbeded()
                        elif botChoice == "paper":
                            yes = {}
                            for cur_currency in rps["currencies"]:
                                maximum = rps["currencies"][cur_currency][0]
                                minimum = rps["currencies"][cur_currency][1]
                                randomMoney = random.randint(maximum,minimum)
                                yes[cur_currency] = randomMoney
                                await give_money(ctx.author,cur_currency,randomMoney)
                            await sendWinEmbeded(yes)
                    elif playerMessage.content.lower() == "rock":
                        if botChoice == "paper":
                            yes = {}
                            for cur_currency in rps["currencies"]:
                                maximum = rps["currencies"][cur_currency][0]
                                minimum = rps["currencies"][cur_currency][1]
                                randomMoney = random.randint(maximum,minimum)
                                yes[cur_currency] = -randomMoney
                                await give_money(ctx.author,cur_currency,-randomMoney)
                            await sendLoseEmbeded(yes)
                        elif botChoice == "rock":
                            await sendTieEmbeded()
                        elif botChoice == "scissors":
                            yes = {}
                            for cur_currency in rps["currencies"]:
                                maximum = rps["currencies"][cur_currency][0]
                                minimum = rps["currencies"][cur_currency][1]
                                randomMoney = random.randint(maximum,minimum)
                                yes[cur_currency] = randomMoney
                                await give_money(ctx.author,cur_currency,randomMoney)
                            await sendWinEmbeded(yes)
                    elif playerMessage.content.lower() == "paper":
                        if botChoice == "scissors":
                            yes = {}
                            for cur_currency in rps["currencies"]:
                                maximum = rps["currencies"][cur_currency][0]
                                minimum = rps["currencies"][cur_currency][1]
                                randomMoney = random.randint(maximum,minimum)
                                yes[cur_currency] = -randomMoney
                                await give_money(ctx.author,cur_currency,-randomMoney)
                            await sendLoseEmbeded(yes)
                        elif botChoice == "paper":
                            await sendTieEmbeded()
                        elif botChoice == "rock":
                            yes = {}
                            for cur_currency in rps["currencies"]:
                                maximum = rps["currencies"][cur_currency][0]
                                minimum = rps["currencies"][cur_currency][1]
                                randomMoney = random.randint(maximum,minimum)
                                yes[cur_currency] = randomMoney
                                await give_money(ctx.author,cur_currency,randomMoney)
                            await sendWinEmbeded(yes)
                    else:
                        await ctx.send(f"{playerMessage.content} is not a paper, scissor, or rock.")
                        return
            except asyncio.TimeoutError:
                await ctx.send("Cancelling due to timeout error", delete_after=7)
    if coinFlip['bool'] == True:
        @commands.command(aliases=["flipcoin", "fc", "cf", "cflip", "fcoin", "flip"])
        @commands.cooldown(1, coinFlip["cooldown"], commands.BucketType.user)
        async def coinflip(self, ctx):
            async def give_money(user,currency,amount):
                with open(usersDir) as f:
                    users = json.load(f)
                    users[f"{user.id}"][currency] += amount
                with open(usersDir, "w") as f:
                    json.dump(users, f, indent=4)

            #Vars
            randomFlip = random.randint(1, 2)
            randomMoney = None

            #Win Message
            async def sendWinEmbeded(mAmt):
                mAmtString = []
                for i in mAmt:
                    mAmtString.append(f"`{str(i)}: {str(mAmt[i])}` \n")
                winEmbeded = discord.Embed(
                    colour=discord.Color.green(),
                    title='**YOU WON COINFLIP**',
                    description=f"{coinFlip['other_args']['messages'][0]} \n You win:\n {' '.join(mAmtString)}"
                )
                await ctx.send(embed=winEmbeded)
            
            #Lose Message
            async def sendLoseEmbeded(mAmt):
                mAmtString = []
                for i in mAmt:
                    mAmtString.append(f"`{str(i)}: {str(mAmt[i])}` \n")
                loseEmbeded = discord.Embed(
                    colour=discord.Color.red(),
                    title='**YOU LOST COINFLIP**',
                    description=f"{coinFlip['other_args']['messages'][1]} \n You lost:\n {' '.join(mAmtString)}"
                )
                await ctx.send(embed=loseEmbeded)

            try:
                await ctx.send(f"Please choose between `heads` or `tails`")

                #Waits for someone's message
                playerMessage = await self.client.wait_for(
                    "message",
                    timeout=30,
                    check=lambda m: m.author == ctx.author and m.channel == ctx.channel
                )

                #Heads
                if playerMessage.content.lower() == "heads":
                    if randomFlip == 2:
                        yes = {}
                        for cur_currency in coinFlip["currencies"]:
                            maximum = coinFlip["currencies"][cur_currency][0]
                            minimum = coinFlip["currencies"][cur_currency][1]
                            randomMoney = random.randint(maximum,minimum)
                            yes[cur_currency] = randomMoney
                            await give_money(ctx.author,cur_currency,randomMoney)
                        await sendWinEmbeded(yes)
                    else:
                        yes = {}
                        for cur_currency in coinFlip["currencies"]:
                            maximum = coinFlip["currencies"][cur_currency][0]
                            minimum = coinFlip["currencies"][cur_currency][1]
                            randomMoney = random.randint(maximum,minimum)
                            await give_money(ctx.author,cur_currency,-randomMoney)
                        await sendLoseEmbeded(yes)
                #Tails
                elif playerMessage.content.lower() == "tails":
                    if randomFlip == 1:
                        yes = {}
                        for cur_currency in coinFlip["currencies"]:
                            maximum = coinFlip["currencies"][cur_currency][0]
                            minimum = coinFlip["currencies"][cur_currency][1]
                            randomMoney = random.randint(maximum,minimum)
                            await give_money(ctx.author,cur_currency,randomMoney)
                        await sendWinEmbeded(yes)
                    else:
                        yes = {}
                        for cur_currency in coinFlip["currencies"]:
                            maximum = coinFlip["currencies"][cur_currency][0]
                            minimum = coinFlip["currencies"][cur_currency][1]
                            randomMoney = random.randint(maximum,minimum)
                            await give_money(ctx.author,cur_currency,-randomMoney)
                        await sendLoseEmbeded(yes)
            #Timeout(30 sec)
            except asyncio.TimeoutError:
                await ctx.send("Cancelling due to timeout error", delete_after=7)

def setup(client):
    client.add_cog(Minigames(client))