import discord
from discord.ext import commands
bot = commands.Bot(command_prefix = '#')
token = open("token", "r").readline()

@bot.command(aliases = ['write'])
async def writing_(ctx, *, message):
    text=message + '<br>\n'
    with open("C:/Users/PC/Desktop/HTML/sowon.html", 'a', encoding="UTF-8") as file:    
        file.write(text)



bot.run('token')












