from discord.ext import commands
import discord
import os
import random
import requests


intents = discord.Intents.default()
intents.message_content = True

#prefijo del bot "$""
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Tu bot {bot.user} esta en linea')


@bot.command()
async def cmd(ctx):
    await ctx.send("""
$cmd
$saludo
$despedida "chao, bye, nos vemos"
$roll XdY   (X, Y, valores a cambiar por numeros)
$add x + y + ... + ... ... ...
$memes
$duck
    """)

@bot.command()
async def saludo(ctx):
    await ctx.send('Hola')

#@bot.command()
async def despedida(ctx, *, mensaje: str):
    mensaje = mensaje.lower()

    if 'chao' in mensaje:
        await ctx.send('Adios')
    elif 'bye' in mensaje:
        await ctx.send('Goodbye')
    elif 'nos vemos' in mensaje:
        await ctx.send('te cuidas')

#Genera un dado y muestra los respectivos resultados de los dados
@bot.command()
async def roll(ctx, dice: str): #   $roll
    try:
        dados_lanzados, caras_dado = map(int, dice.split('d'))
    except Exception:
        await ctx.send('¡El formato correcto es NdN! Ejemplo: 2d6 (2 dados de 6 caras).') # Sale esto si el formato de dado es incorrecto
        return

    resultado = ', '.join(str(random.randint(1, caras_dado)) for r in range(dados_lanzados))
    await ctx.send(f' **Tus dados cayeron en:** {resultado}')

#Agarra todos los numeros colocados y los deja en una lista, luego de eso suma todos los numeros
@bot.command()
async def add(ctx, *numeros: int):
    """Suma todos los números que le envíes."""
    # Verificamos si el usuario eligio mas de 1 numero
    if not numeros:
        await ctx.send("¡Tienes que escribir al menos dos números! Ejemplo: `$add 5 10 3`")
        return

    # sum() es una función que hace que los numeros de la lista se sumen
    resultado = sum(numeros)
    
    # Creamos un texto para mostrar el resultado
    # Ejemplo: "5 + 10 + 3"
    operacion = " + ".join(map(str, numeros))
    
    await ctx.send(f"**Suma:** {operacion} = **{resultado}**")


#Token de discord
token=""

bot.run(token)
