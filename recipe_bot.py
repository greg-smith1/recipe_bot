import os
import time
import asyncio
import model

import discord

DISCORD_BOT_TOKEN = os.environ.get('RECIPE_BOT_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print('----------------')
    print('  Logged in as  ')
    print(client.user.name)
    print(client.user.id)
    print('----------------')
    print('\n')

@client.event
async def on_message(message):
    print(message.content, message.channel, message.author.name, 
          message.author.id, type(message.author.id), type(message.author))
    
    if message.content.startswith('!random'):
        with Apiwrapper() as wrapper:
            #TODO get length of Database
            #TODO get random number to snag recipe index
            recipe = wrapper.select_recipe(random_num)
        await client.send_message(message.channel, recipe.title)

    elif message.content.startswith('!recipe'):
        name = message.content.split()[1:].join()
        with Apiwrapper() as wrapper:
            recipe = wrapper.select_recipe(name)
            if recipe:
                await client.send_message(message.channel, recipe.title)
            else:
                await client.send_message(message.channel, "Couldn't find that one")

