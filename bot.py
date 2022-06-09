import discord
from discord.ext import commands

bot=commands.Bot(command_prefix = "k" )

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)}ms")


bot.run("OTg0MzUwNTg5MjUxMTA0ODE4.GrSSjB.sRFFdSZP_2dN1QWsWZBGaZEOJAhbqI6S__Mi24") 





