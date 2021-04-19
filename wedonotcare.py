import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='+',  self_bot=True)
        
@bot.command()
async def wedontcare(ctx, userid):
    await ctx.send(f"Hey <@{userid}>", file=discord.File("video.mov"))

bot.run("put your token here", bot=False)
