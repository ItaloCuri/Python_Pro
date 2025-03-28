import discord  # Librería oficial de Discord para interactuar con su API
from discord.ext import commands  # Módulo que facilita la creación de comandos para el bot

# 🔹 Configuración de los permisos del bot
# "Intents" son permisos especiales que permiten al bot acceder a ciertos eventos en Discord.
# Por ejemplo, leer mensajes, ver usuarios en línea, etc.
intents = discord.Intents.default()  # Se activan los permisos básicos del bot
intents.message_content = True  # Se activa el permiso para que el bot pueda leer mensajes

# 🔹 Creación del bot
# "command_prefix" define con qué símbolo deben comenzar los comandos (en este caso, "$")
bot = commands.Bot(command_prefix="$", intents=intents)

# 🔹 Evento cuando el bot está listo
# "@bot.event" indica que esta función reacciona a un evento especial de Discord.
# En este caso, el evento "on_ready" se activa cuando el bot se conecta exitosamente.
@bot.event
async def on_ready():
    print(f'✅ Hemos iniciado sesión como {bot.user}')  # Muestra el nombre del bot en la consola

# 🔹 Comando "$kodland" para mandar un emoji
# "@bot.command()" define un nuevo comando que el bot reconocerá
@bot.command()
async def kodland(ctx):  # "ctx" representa el contexto del comando (información sobre quién lo ejecutó, dónde, etc.)
    await ctx.send("\U0001f642")  # Código Unicode para el emoji "🙂"
    
#devolver  lo que el usuario escriba
@bot.command()
async def repetir(ctx, *, message: str):
    # "*" permite que el usuario escriba varias palabras y no solo una
    # "message: str" indica que el parámetro será una cadena de texto (string)
    await ctx.send(message)  # Envía el mismo mensaje que el usuario escribió

# 🔹 Comando "$saludo" para responder a diferentes tipos de saludos
@bot.command()
async def saludo(ctx, *, mensaje: str):
    mensaje = mensaje.lower().strip()  # Convierte el mensaje a minúsculas y elimina espacios extra

    # Comprobamos si el mensaje contiene ciertas palabras clave
    if "hola" in mensaje:
        await ctx.send("¡Hola! ¿Cómo estás? 😊")
    elif "adiós" in mensaje:
        await ctx.send("¡Hasta luego! 👋")
    elif "gracias" in mensaje:
        await ctx.send("¡De nada! 😃")
    else:
        await ctx.send("No entendí tu saludo. 😕")  # Si no reconoce la palabra, responde con un mensaje neutral

# 🔹 Comando "$emocion" para responder a estados emocionales del usuario
@bot.command()
async def emocion(ctx, *, mensaje: str):
    mensaje = mensaje.lower().strip()  # Convierte el mensaje a minúsculas y elimina espacios extra
    
    # Si el usuario menciona "triste", el bot responde con un mensaje motivador
    if 'triste' in mensaje:
        await ctx.send('''No todos los días son felices, pero podemos hacerlos mejores. 
        Intenta salir de casa, a veces estar encerrado nos hace enfocarnos en el dolor.''')
    
    # Si el usuario menciona "feliz", el bot responde con un mensaje de alegría
    elif 'feliz' in mensaje:
        await ctx.send('''Me alegro de que estés feliz. Para sumarle entusiasmo a mi felicidad, 
        me gusta comer una buena hamburguesita 🍔''')
        
    else:
        await ctx.send('No entendi tu emocion pero recuerda que al mal tiempo buena cara 😃')

# 🔹 Token del bot (IMPORTANTE: No compartir con nadie)
# El token es como la "contraseña" del bot, necesaria para conectarlo a Discord.

token = "pon_tu_token_aqui"

# 🔹 Iniciar el bot
# Esta línea conecta el bot a Discord y lo mantiene en ejecución.



@bot.command()
async def repeat(ctx, times: int, *, content: str):
    # """Repite un mensaje varias veces."""
    for _ in range(times):
        await ctx.send(content)


@bot.command()
async def add(ctx, left: int, right: int):
    #"""Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def mult(ctx, left: int, right: int):
    #"""multiply two numbers together."""
    await ctx.send(left * right)

@bot.command()
async def div(ctx, left: int, right: int):
    #"""divide two numbers together."""
    await ctx.send(left / right)

@bot.command()
async def min(ctx, left: int, right: int):
    #"""min two numbers together."""
    await ctx.send(left - right)

bot.run(token)
