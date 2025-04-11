import discord  # Librería oficial de Discord para interactuar con su API
import random #Liberia Oficial de Python para colocar algo al azar
from discord.ext import commands  # Módulo que facilita la creación de comandos para el bot

Ideas = [
    "Plantar un árbol en tu barrio",
    "Reciclar papel y plástico en casa",
    "Apagar las luces cuando no se usan",
    "Hacer una campaña para limpiar un parque",
    "Enseñar a otros a cuidar el planeta"
]

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
    elif "adiós" or "adios" in mensaje:
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

token = '########################' #pon aca tu token

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


@bot.command()
async def mem(ctx):
    
    with open('imagen/mem1.jpeg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
    
# como listar archivos dentro de una carpeta.
import os  

# Importamos la librería 'random' que nos ayuda a elegir elementos al azar,
# en este caso, seleccionará una imagen aleatoria de una carpeta.
import random   

# Definimos un comando en nuestro bot con @bot.command()
# Cuando un usuario escriba !meme_aleatorio en el chat de Discord, el bot ejecutará esta función.
@bot.command()
async def meme_aleatorio(ctx):  
    """
    Esta función elige una imagen aleatoria de la carpeta 'imagenes'
    y la envía al canal de Discord cuando el usuario escribe !meme_aleatorio.
    ctx representa el contexto del comando, es decir, información sobre quién ejecutó el comando
    y en qué canal se ejecutó.
    """

    # Usamos os.listdir('imagenes') para obtener una lista con todos los nombres de archivos
    # que hay dentro de la carpeta 'imagenes'.
    # Luego, usamos random.choice() para elegir aleatoriamente uno de esos archivos.
    img_name = random.choice(os.listdir('imagen'))  

    # Abrimos el archivo de imagen seleccionado en modo lectura binaria ('rb').
    # 'f'imagenes/{img_name}' permite construir la ruta del archivo dinámicamente,
    # reemplazando {img_name} con el nombre de la imagen seleccionada.
    with open(f'imagen/{img_name}', 'rb') as f:  
        picture = discord.File(f)  # Creamos un objeto de tipo File que representa la imagen.

    # Enviamos la imagen al canal donde se escribió el comando.
    # 'await' se usa porque enviar un archivo es una tarea asíncrona,
    # lo que significa que el bot puede seguir funcionando sin bloquearse.
    await ctx.send(file=picture) 
    
    

import requests  

# Definimos una función para obtener la URL de una imagen de pato aleatoria.
def obtener_imagen_pato():    
    """
    Esta función se conecta a una API que devuelve imágenes aleatorias de patos.
    Retorna la URL de la imagen para que el bot la pueda enviar.
    """

    # URL de la API que nos da imágenes aleatorias de patos.
    url = 'https://random-d.uk/api/random'

    # Hacemos una solicitud GET a la API para obtener información.
    respuesta = requests.get(url)

    # Convertimos la respuesta de la API en un diccionario de Python.
    datos = respuesta.json()  

    # Extraemos la URL de la imagen del diccionario y la retornamos.
    return datos['url']


# Definimos un comando en nuestro bot con @bot.command()
# Cuando un usuario escriba !pato en el chat de Discord, el bot ejecutará esta función.
@bot.command(name='pato')  # Cambiamos el nombre del comando a 'pato' para mantener la coherencia.
async def enviar_pato(ctx):  
    """
    Esta función obtiene una imagen aleatoria de un pato y la envía al canal de Discord.
    Se activa cuando un usuario escribe !pato en el chat.
    """

    # Llamamos a la función 'obtener_imagen_pato' para obtener la URL de la imagen.
    url_imagen = obtener_imagen_pato()  

    # Enviamos la imagen al canal donde se escribió el comando.
    # 'await' es necesario porque ctx.send() es una función asíncrona,
    # lo que significa que el bot espera a que se complete antes de continuar con otras tareas.
    await ctx.send(url_imagen)

@bot.command(name="idea")
async def idea(ctx, *, mensaje: str):
    mensaje = mensaje.lower().strip()

    if "ambiental" in mensaje:
        idea_aleatoria = random.choice(Ideas)
        await ctx.send(f"🌿 Idea ambiental: {idea_aleatoria}")
    else:
        await ctx.send("¿Querías una idea ambiental? Escribe: `$idea ambiental` 🌎")

bot.run(token)
