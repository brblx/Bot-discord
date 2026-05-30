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
    """
#Cosas main2
"""
$frase
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


@bot.command()
async def memes(ctx):

    #meme1 o meme2 o meme3 .png
    img_name= random.choice(os.listdir('imagenes'))

    with open(f'imagenes/{img_name}', 'rb') as f:

        picture = discord.File(f)

        await ctx.send(file = picture)



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


#Cosas main2

frases_ambientales = [
    "Cuidar el planeta no es una opción, es nuestra obligación. Pequeñas acciones hoy aseguran el mañana.",
    "La Tierra no nos pertenece, nosotros pertenecemos a la Tierra. Respeta cada rincón de la naturaleza.",
    "Mucha gente pequeña, en lugares pequeños, haciendo cosas pequeñas, puede cambiar el mundo. ¡Empieza por reducir y reciclar!",
    "La naturaleza no necesita de los seres humanos, pero nosotros sí necesitamos desesperadamente de ella.",
    "Convertir un árbol en leña es fácil, pero ningún ser humano puede devolverle sus hojas. Protege nuestros bosques.",
    "El agua es la fuerza motriz de toda la naturaleza. No la desperdicies hoy si quieres tener un mañana."
]

@bot.command()
async def frase(ctx):
    frase_elegida = random.choice(frases_ambientales)
    await ctx.send(f"Mensaje ecologico: {frase_elegida}")

    
#Token de discord
token=""

bot.run(token)
