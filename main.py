import discord
from config import token
bot = discord.Client()
@bot.event
async def on_message(message):
    if str(message.channel) == 'img' and message.content != "":
        await message.channel.purge(limit=1)
bot.run(token)
