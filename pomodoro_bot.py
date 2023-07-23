

#!pip install discord
#!pip install nest_asyncio

import discord
import asyncio
from collections import Counter
import nest_asyncio

intents = discord.Intents().all()

palavras = []
contagem = Counter()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('!pomodoro'):
        args = message.content.split(' ')
        focus_time = int(args[1]) * 60  # in seconds
        break_time = int(args[2]) * 60  # in seconds

        await message.channel.send(f'{message.author.mention} O temporizador Pomodoro foi iniciado com {args[1]} minutos de foco e {args[2]} minutos de pausa.')

        await asyncio.sleep(focus_time)
        await message.channel.send(f'{message.author.mention} Tempo de foco terminou. Hora da pausa!')
        await asyncio.sleep(break_time)
        await message.channel.send(f'{message.author.mention} Tempo de pausa acabou. Começando outro ciclo de {args[1]} minutos de foco.')

nest_asyncio.apply()
client.run('//Sua Key')
