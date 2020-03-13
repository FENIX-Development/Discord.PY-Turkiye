import discord
import os
from discord.ext import commands, tasks
from cevrimici.onlinebot import onlinebot
from dotenv import load_dotenv

load_dotenv()
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
  print('Bot çevrimiçi!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

onlinebot()
token = os.environ.get("TOKEN") 
client.run(token)