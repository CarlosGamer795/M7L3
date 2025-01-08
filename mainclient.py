import discord
import random

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)
correct_answer = None

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    global correct_answer  # Declarar la variable global para su uso
    if message.author == client.user:
        return
    
    content = message.content.lower()
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$adivinanza'):
        riddles = [
            ("¿Qué cosa será, qué cosa es? Que cuanto más seca está, más moja pies.", "la toalla"), 
            ("Tiene ojos y no puede ver, tiene agua y no puede beber.", "el mar")
        ]
        riddle, answer = random.choice(riddles)
        correct_answer = answer.lower()
        await message.channel.send(riddle)
    elif correct_answer and content == correct_answer:
        await message.channel.send("¡Adivinaste!")
        correct_answer = None  # Respuesta correcta encontrada, resetear la respuesta correcta
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    else:
        await message.channel.send(message.content)


        
client.run(#Inserte el token de dicord entre comillas
    )