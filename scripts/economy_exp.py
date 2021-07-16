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
#

intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents,owner_id=owner_id)

usersDir = os.path.join("JSON_FILES", "users.json")

class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client
    #START ECONOMY GENERATION HERE
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        async def update_data(users, user):
            if not f"{user.id}" in users:
                users[f"{user.id}"] = {}
                # exp/lvl
                users[f"{user.id}"]["experience"] = 0
                users[f"{user.id}"]["level"] = 0
                # currency
                for cur in currency:
                    print(cur)
                    users[f"{user.id}"][cur] = 0
        with open(usersDir, 'r') as f:
            users = json.load(f)
        await update_data(users, member)
        with open(usersDir, 'w') as f:
            json.dump(users, f, indent=4)
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        async def update_data(users, user):
            if not f"{user.id}" in users:
                users[f"{user.id}"] = {}
                # exp/lvl
                users[f"{user.id}"]["experience"] = 0
                users[f"{user.id}"]["level"] = 0
                # currency
                for cur in currency:
                    print(cur)
                    users[f"{user.id}"][cur] = 0
        async def add_experience(users, user, amt):
            pass
        async def level_up(users, user, msg):
            pass
        if msg.author.bot == False:
            with open(usersDir, "r") as f:
                users = json.load(f)
            await update_data(users, msg.author)
            await add_experience(users, msg.author, random.randint(2, 7))
            await level_up(users, msg.author, msg)

            with open(usersDir, "w") as f:
                json.dump(users, f, indent=4)



def setup(client):
    client.add_cog(Economy(client))