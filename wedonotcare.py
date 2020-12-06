import discord
from discord.ext import commands


Fuckyou = 'YourID Here'
bot = commands.Bot(command_prefix='+',  self_bot=True)


@bot.event
async def on_message(message) :
    if message.author.id == Fuckyou :
        
        await message.channel.send("Hey <@{}>!".format(Fuckyou), file=discord.File("video.mov"))


bot.run("Mzk1NzUwMjUzNjQ0NjExNTg1.X8wbwg.MgYgoSvK1Pfp7xvp_MPLJj0BCuc", bot = False)



