import discord
from discord.ext import commands

class ping(commands.Cog):
  
  def __init__(self, client):
    self.client = client
    
  @commands.command()
  async def ping(self, ctx):
    await ctx.send(f'{round(ctx.bot.latency * 1000)} ms')
    
def setup(client):
  client.add_cog(ping(client))