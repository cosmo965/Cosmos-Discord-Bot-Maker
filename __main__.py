import sys
from generator_main import discord_python_file
import ast
import json

r"""
Transporting data format-
bot_name=["Free robux bot"]
owner_id=['35042005424']
token=['35_dert4442']
client_id=['3456542']
directory=(directory) [e.g: {C:\Users\chevr\Desktop\Python projects\Cosmo productions\applications} ]
minigames={'rps': {'bool':True, 'currencies':{"":[None,None],"free":[34,None]}, 'other_args':{"messages":["","",""]}},'coinFlip':{'bool':False, 'currencies':{}, 'other_args':{}}}
currency=['Coins', 'Gems']
bot_commands={'balance':True}
"""

discord_python_file(
    bot_name        = ast.literal_eval(sys.argv[1]),
    owner_id        = ast.literal_eval(sys.argv[2]),
    token           = ast.literal_eval(sys.argv[3]),
    client_id       = ast.literal_eval(sys.argv[4]),
    directory       = ast.literal_eval(sys.argv[5]),
    minigames       = ast.literal_eval(sys.argv[6]),
    currency        = ast.literal_eval(sys.argv[7]),
    bot_commands    = ast.literal_eval(sys.argv[8]),
)
