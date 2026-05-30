import discord
from discord.ext import commands
import random


intents = discord.Intents.default()
intents.message_content = True

#prefijo del bot "$""
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Tu bot {bot.user} esta en linea')

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


@bot.command()
async def cmd(ctx):
    await ctx.send("""
$cmd
$frase
    """)


#Token de discord
token=""

bot.run(token)
