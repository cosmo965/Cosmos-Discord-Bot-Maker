import os
import re


class discord_python_file():
    def __init__(self,bot_name,owner_id,token,client_id,directory,minigames,currency,bot_commands):
        #Initiation
        current_code_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
        os.chdir(current_code_dir)
        MainBot_PY = None
        CREATED_BOTS_FolderName = "CREATED_BOTS-cosmo-discord-bot"
        scripts_directory = os.path.join(os.getcwd(),"scripts")

        self.bot_commands = bot_commands
        self.minigames = minigames
        self.currency = currency
        self.botname = bot_name
        self.clientid = client_id
        self.directory = directory
        self.owner_id = owner_id
        self.token = token

        string_iter = {
            "minigames": self.minigames,
            "bot_commands": self.bot_commands,
            "currency": self.currency,
            "botname": self.botname,
            "clientid": self.clientid,
            "directory": self.directory,
            "owner_id": self.owner_id,
            "token": self.token,
        }

        print(f"{str(self.botname[0].upper())} || INITIATION{os.linesep}CLIENT-ID: {self.clientid}{os.linesep}OWNER-ID: {self.owner_id}{os.linesep}TOKEN: {self.token}{os.linesep}DIRECTORY: {self.directory}{os.linesep}MINIGAMES: {self.minigames}{os.linesep}CURRENCY: {self.currency}{os.linesep}BOT COMMANDS: {self.bot_commands}{os.linesep}")
        
        #Creating the base directory for bots
        if not os.path.exists(fr"{self.directory[0]}\{CREATED_BOTS_FolderName}"):
            os.chdir(fr"{self.directory[0]}")
            ApplicationBotsFolder = os.mkdir(CREATED_BOTS_FolderName)
        #Creating the base files requested by the client
        if not os.path.exists(fr"{self.directory[0]}\{CREATED_BOTS_FolderName}\{self.botname[0]}"):
            os.chdir(fr"{self.directory[0]}\{CREATED_BOTS_FolderName}")
            MainBot_PY = os.mkdir(str(self.botname[0]))
        #Creating the cog file for the base file
        if not os.path.exists(fr"{self.directory[0]}\{CREATED_BOTS_FolderName}\{self.botname[0]}\cogs"):
            os.chdir(fr"{self.directory[0]}\{CREATED_BOTS_FolderName}\{self.botname[0]}")
            CogFolder = os.mkdir("cogs")
        #Creating the JSON folder for the base file
        if not os.path.exists(fr"{self.directory[0]}\{CREATED_BOTS_FolderName}\{self.botname[0]}\JSON_FILES"):
            os.chdir(fr"{self.directory[0]}\{CREATED_BOTS_FolderName}\{self.botname[0]}")
            JsonFilesFolder = os.mkdir("JSON_FILES")
        # Resets current directory for generation below
        os.chdir(self.directory[0])

        #Generation
        
        minigames_lines = []
        main_py_lines = []
        currencies_py_lines = []
        bot_cmds_py_lines = []
        
        with open(os.path.join(scripts_directory,"minigames.py"),'r') as file:
            for line in file:
                minigames_lines.append(line)
        with open(os.path.join(scripts_directory,"main.py"),'r') as file:
            for line in file:
                main_py_lines.append(line)
        with open(os.path.join(scripts_directory,"economy_exp.py"),'r') as file:
            for line in file:
                currencies_py_lines.append(line)
        with open(os.path.join(scripts_directory,"other_commands.py"),'r') as file:
            for line in file:
                bot_cmds_py_lines.append(line)
        
        MainBot_PY = open(os.path.join(fr"{self.directory[0]}\{CREATED_BOTS_FolderName}\{self.botname[0]}", "main.py"),'w')
        MinigamesBot_PY = open(os.path.join(fr"{self.directory[0]}\{CREATED_BOTS_FolderName}\{self.botname[0]}\cogs", "minigames.py"),'w')
        Currencies_PY = open(os.path.join(fr"{self.directory[0]}\{CREATED_BOTS_FolderName}\{self.botname[0]}\cogs", "economy.py"),'w')
        Bot_Cmds_PY = open(os.path.join(fr"{self.directory[0]}\{CREATED_BOTS_FolderName}\{self.botname[0]}\cogs", "other_commands.py"),'w')

        os.chdir(fr"{self.directory[0]}\{CREATED_BOTS_FolderName}\{self.botname[0]}\JSON_FILES")
        Users_JSON = open("users.json", 'w')
        Levels_JSON = open("levels.json", 'w')
        Prefixes_JSON = open("prefixes.json", 'w')
        os.chdir(self.directory[0])

        # JSON
        Users_JSON.write("{}")
        Levels_JSON.write("{}")
        Prefixes_JSON.write("{}")

        # MINIGAMES GENERATE
        for line in minigames_lines:
            if " #editable" in str(line):
                try:
                    divided = str(line).split(' =')
                    current_values = str(self.minigames[divided[0].split(" ")[0]])
                    final_text = f"{divided[0]} = {current_values}"
                    MinigamesBot_PY.write(f"{final_text} #EDITED \n")
                except Exception:
                    divided = str(line).split(' =')
                    current_values = str(string_iter[divided[0].lower()])
                    final_text = f"{divided[0]} = {current_values}"
                    MinigamesBot_PY.write(f"{final_text} #EDITED \n")
            else:
                MinigamesBot_PY.write(line)
        # MAIN.PY GENERATE
        for line in main_py_lines:
            if " #editable" in str(line):
                try:
                    divided = str(line).split(' =')
                    current_values = str(string_iter[divided[0]])
                    final_text = f"{divided[0]} = {current_values}"
                    MainBot_PY.write(f"{final_text} #EDITED \n")
                except Exception:
                    divided = str(line).split(' =')
                    current_values = str(string_iter[divided[0].lower()])
                    final_text = f"{divided[0]} = {current_values}"
                    MainBot_PY.write(f"{final_text} #EDITED \n")
                    pass
            else:
                MainBot_PY.write(line)
        # ECONOMY/EXP GENERATE
        for line in currencies_py_lines:
            if " #editable" in str(line):
                try:
                    divided = str(line).split(' =')
                    current_values = str(string_iter[divided[0]])
                    final_text = f"{divided[0]} = {current_values}"
                    Currencies_PY.write(f"{final_text} #EDITED \n")
                except Exception:
                    divided = str(line).split(' =')
                    current_values = str(string_iter[divided[0].lower()])
                    final_text = f"{divided[0]} = {current_values}"
                    Currencies_PY.write(f"{final_text} #EDITED \n")
                    pass
            else:
                Currencies_PY.write(line)
        
        # BOT COMMANDS GENERATE
        for line in bot_cmds_py_lines:
            if " #editable" in str(line):
                try:
                    divided = str(line).split(' =')
                    current_values = str(string_iter[divided[0]])
                    final_text = f"{divided[0]} = {current_values}"
                    Bot_Cmds_PY.write(f"{final_text} #EDITED \n")
                except Exception:
                    pass
            else:
                Bot_Cmds_PY.write(line)
        
        # CLOSING/SAVING OPENED FILES

        Users_JSON.close()
        Levels_JSON.close()
        Prefixes_JSON.close()
        Currencies_PY.close()
        MinigamesBot_PY.close()
        MainBot_PY.close()
        Bot_Cmds_PY.close()