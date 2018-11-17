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
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot is ready and comected to discord!')
    
@client.command()
async def hosting():
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Hosting')
    
    embed.add_field(name = '``Support Server`` ',value ='https://discord.gg/V6EA2M',inline = False)
    embed.add_field(name = 'Github',value ='https://www.github.com',inline = False)
    embed.add_field(name = 'Heroku',value ='https://www.heroku.com',inline = False)
    await client.say(embed=embed)
    
@client.command()
async def help():
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Help')
    
    embed.add_field(name = '``Žádné příkazy nebily nalezeny! (Zatim)`` ',value ='Support Server: https://discord.gg/V6EA2M',inline = False)
    
@client.event
async def on_member_join(member):
    print("In our server" + member.name + " just joined")
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Welcome message')
    embed.add_field(name = '__Vítej na MineTeam CZ SK!__',value ='**Přečti si pravidla a neporušuj je! Doufám že budeš aktivní! :)',inline = False)
    embed.set_image(url = 'https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')
    await client.send_message(member,embed=embed)
    print("Sent message to " + member.name)
    channel = discord.utils.get(client.get_all_channels(), server__name='MineTeam CZ SK', name='welcome')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Do not forget to check <#474572305192845312> and never try to break any one of them', color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name='__Díky že ses připojil!__', value='**Doufám že tu budeš aktivní ;).**', inline=True)
    embed.add_field(name='Připojil ses jako', value=member.joined_at)
    embed.set_image(url = 'https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')
    embed.set_thumbnail(url=member.avatar_url)
    await client.send_message(channel, embed=embed)

    
client.run(os.getenv("BOT_TOKEN"))
