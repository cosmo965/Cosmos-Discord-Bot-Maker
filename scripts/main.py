import discord
from discord.ext import commands
import random
import math
import json
import os
import sys



# SETTINGS
owner_id = ["owner_id"] #editable
TOKEN = ["token"] #editable
directory = ["directory"] #editable
botname = ["botname"] #editable
#

os.chdir(os.path.dirname(__file__))
print(f"The current directory is; [{os.getcwd()}]")

prefixDir = os.path.join("JSON_FILES", "prefixes.json")

def getPrefix(client, message):
    try:
        with open(prefixDir, 'r') as f:
            prefixes = json.load(f)
            return prefixes[str(message.guild.id)]
    except KeyError:
        with open(prefixDir, 'r') as k:
            prefixes = json.load(k)
        prefixes[str(message.guild.id)] = '.'
        with open(prefixDir, 'w') as j:
            json.dump(prefixes, j, indent = 4)
        with open(prefixDir, 'r') as t:
            prefixes = json.load(t)
            return prefixes[str(message.guild.id)]
    except:
        return '.'

intents = discord.Intents.all()
client = commands.Bot(command_prefix=getPrefix,intents=intents, owner_id=owner_id[0])
client.remove_command('help')
member = discord.Member

@client.event
async def on_guild_join(guild):
    with open(prefixDir, "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "."

    with open(prefixDir, "w") as f:
        json.dump(prefixes, f, indent=4)
@client.event
async def on_guild_remove(guild):
    with open(prefixDir, "r") as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open(prefixDir, "w") as f:
        json.dump(prefixes, f, indent=4)
@client.command()
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, prefix):
    with open(prefixDir, "r") as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix
    with open(prefixDir, "w") as f:
        json.dump(prefixes, f, indent=4)
    prefixChange = discord.Embed(
        colour=random.randint(0, 0xffffff),
        title='Prefix',
        description=f"The prefix for **{ctx.guild.name}** is now `{prefix}`"
    )
    await ctx.send(embed=prefixChange)
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=".help"))
    print(f"Logged on as {client.user}")
@client.command()
async def logout(ctx):
    memberID = ctx.message.author
    userID = memberID.id
    if userID == 340940207744614400:
        await ctx.send(f"{ctx.author.mention}, imagine making me logout. >:C", delete_after=2)
        await client.logout()
    elif userID == 451439727820668929:
        await ctx.send(f"{ctx.author.mention}, imagine making me logout. >:C", delete_after=2)
        await client.logout()
    else:
        await ctx.send("You are not the owner of this bot. Smh")
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=".help"))
    print(f"Logged on as {client.user}")

client.run(TOKEN[0])