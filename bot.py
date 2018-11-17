import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import platform
import colorsys
import random
import os
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType

client = commands.Bot(command_prefix = '?')

@client.event
async def on_ready():
    print('Bot is ready and comected to discord!')
    
@client.command()
async def hosting():
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Hosting')
    embed.set_image(url = 'https://cdn.discordapp.com/attachments/444585767210057728/513149361027284992/1_Bwp5z9qlQAor4hw2K61gIw.jpeg')
    embed.add_field(name = '``Support Server`` ',value ='https://discord.gg/A36parZ',inline = False)
    embed.add_field(name = 'Github',value ='https://www.github.com',inline = False)
    embed.add_field(name = 'Heroku',value ='https://heroku.com',inline = False)
    
    await client.say(embed=embed)
    

client.run(os.getenv("BOT_TOKEN"))
