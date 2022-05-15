import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("봇이 시작되었습니다.")

@bot.command()
async def 안녕(ctx):
    await ctx.send('반갑습니다')

bot.run('token')
