import os
import time
import asyncio
import model

import discord

DISCORD_BOT_TOKEN = os.environ.get('RECIPE_BOT_TOKEN')
DB = 'recipes.db'
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
        with model.Database(DB) as rdb:
            #TODO get length of Database
            #TODO get random number to snag recipe index
            sql = """SQL HERE"""
            rdb.cursor.execute(sql)
        await client.send_message(message.channel, 'hi')


