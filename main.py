import os, random
import discord
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
#1
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
#2
def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
#3
def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']
#4
def get_pokemon_image_url():    
    url = 'https://pokeapi.co/api/v2/pokemon/pikachu'
    res = requests.get(url)
    data = res.json()
    return data['sprites']['front_default']
#5
def get_tokio_image_url():    
    url = 'https://kitsu.io/api/edge/anime?filter[text]=tokyo'
    res = requests.get(url)
    data = res.json()
    return data['data'][0]['attributes']['posterImage']['original']
#1
@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
#2
@bot.command('dog')
async def dog(ctx):
    '''Una vez que llamamos al comando dog, 
    el programa llama a la función get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)
#3
@bot.command('fox')
async def fox(ctx):
    '''Una vez que llamamos al comando fox, 
    el programa llama a la función get_fox_image_url'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)
#4
@bot.command('pokemon')
async def pokemon(ctx):
    '''Una vez que llamamos al comando pokemon, 
    el programa llama a la función get_pokemon_image_url'''
    image_url = get_pokemon_image_url()
    await ctx.send(image_url)
#5
@bot.command('tokio')
async def tokio(ctx):
    '''Una vez que llamamos al comando tokio, 
    el programa llama a la función get_tokoi_image_url'''
    image_url = get_tokio_image_url()
    await ctx.send(image_url)

bot.run(#Inserte el token de dicord entre comillas
    )
