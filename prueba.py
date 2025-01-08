import os, random
import discord
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

with open('images/mem1.jpeg', 'rb') as f:
        picture = discord.File(f)