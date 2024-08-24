import discord
import os
from discord.ext import commands
import random
import requests

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Iniciado sesión como {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot de nombre, {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)
    print('Esa es la suma de los numeros que escribiste')

@bot.group()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f'Yes, {ctx.subcommand_passed} is cool')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

@bot.command()
async def imagen1(ctx):
    with open('IMAGENES/imagen1.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def imagen2(ctx):
    imagenes = os.listdir('IMAGENES')
    with open(f'IMAGENES/{random.choice(imagenes)}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def imagen3(ctx):
    with open('IMAGENES/imagen4.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def animal(ctx):
    animales = os.listdir('ANIMALES')
    with open(f'ANIMALES/{random.choice(animales)}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def contaminacion(ctx):
    await ctx.send(f"""¡Hola, soy un bot {bot.user}!""")
    await ctx.send(f'Te voy a hablar un poco sobre la contaminacion')
    await ctx.send(f'La contaminacion es un gran problema a nivel mundial, muchos paises sufren a diario')

    await ctx.send(f"¿Quieres consejos sobre como combatir la contaminacion? Responde con 'si' o 'no':")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['sí', 'si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content in ['sí', 'si']:
            await ctx.send("1. No arrojar basura en los ríos")
            await ctx.send("2. Dejar de quemar basura")
            await ctx.send("3. Aprender a reciclar")
            await ctx.send("4. Disminuir el uso de vehiculos personales como autos o motos")
            await ctx.send("5. No gastando mas de lo debido")
        else:
            await ctx.send("Está bien, pero si alguna vez necesitas consejos, no dudes en preguntar")
    else:
        await ctx.send("Lo siento, pero no puedo entender tu respuesta, Intentalo de nuevo")
    await ctx.send("¿Quieres saber la definicion de contaminacion? Responde con 'si' o 'no':")
    response1 = await bot.wait_for('message', check=check)
    if response1:
        if response1.content in ['sí', 'si']:
            await ctx.send("presencia de un constituyente, impureza o algún otro elemento indeseable que estropea, corrompe, infecta, inutiliza o degrada un material, cuerpo físico, entorno natural, lugar de trabajo, etc")
        else:
            await ctx.send("Está bien, pero si alguna vez necesitas consejos, no dudes en preguntar")
    else:
        await ctx.send("Lo siento, pero no puedo entender tu respuesta, Intentalo de nuevo")

bot.run("bot token")
