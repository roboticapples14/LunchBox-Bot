# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord

# IMPORT THE OS MODULE.
import os

# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv

# IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.
from discord.ext import commands

# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv('.env')

# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = os.getenv("TOKEN")

from groups import *

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    msg = message.content
    # '!lunch' = bot prefix
    if msg.startswith('!lunch'):
        args = msg.split() # input: '!lunch add generate 5', args: ['!lunch', 'add', 'generate', '5'] 
        # ADD USER TO LIST
        if ('add' in args):
            if (add_user(message.author)):
                await message.channel.send('Added ' + str(message.author) + ' to lunchbox list')
            else:
                await message.channel.send(str(message.author) + ' is already on the lunchbox list')

        # REMOVE USER FROM LIST
        if ('remove' in args):
            if (remove_user(message.author)):
                await message.channel.send('Removed ' + str(message.author) + ' from lunchbox list')
            else:
                await message.channel.send(str(message.author) + ' isn\'t in the lunchbox list')

        if ('view' in args):
            # view lunchbox list
            if (len(args) > args.index('view') + 1 and (args[args.index('view') + 1]).lower() == 'lunchbox_list'):
                await message.channel.send('Current Lunchbox List:')
                for i in lunchbox_users:
                    await message.channel.send(str(i) + '\n')
            # view groups
            elif (len(args) > args.index('view') + 1 and (args[args.index('view') + 1]).lower() == 'groups'):
                await message.channel.send('All Generated Lunch Groups:')
                for i, group in enumerate(group_list):
                    if (len(group) > 0):
                        await message.channel.send('\nGroup ' + str(i + 1) + ':')
                        for j in group:
                            await message.channel.send(str(group[j]) + '\n')

        # GENERATE LUNCH GROUP
        if ('generate' in args):
            # default group size is 3
            group_size = 3
            # if argument after generate is an integer, that's size num
            if (len(args) > args.index('generate') + 1 and (args[args.index('generate') + 1]).isdigit()):
                group_size = int(args[args.index('generate') + 1]) # set group size to next argument
            
            lunch_group = generate_group(lunchbox_users, message.author, group_size)
            await message.channel.send('Generated lunch group:')
            for i in lunch_group:
                await message.channel.send(str(i) + '\n')

        if ('help' in args):
            await message.channel.send("Lunchbot is a discord bot to randomly generate lunch groups\n\n")
            await message.channel.send("USAGE\n")
            await message.channel.send("!lunch [help] [add] [remove] [generate (num in group)] [view (lunchbox_list, groups)]\n\n")
            await message.channel.send("OPTIONS:\n")
            await message.channel.send("help:   Program usage and help.\n")
            await message.channel.send("add:    Add yourself to the lunch list.\n")
            await message.channel.send("remove: Remove yourself from the lunch list.\n")
            await message.channel.send("view (lunchbox_list, groups):   View the lunchbox list or the generated groups.\n")
            await message.channel.send("generate (num):     Generate a random lunch group of num people.\n")

client.run(os.getenv('TOKEN'))