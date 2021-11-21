import os
import discord
from discord.ext import commands
from Crypto import crypto

api_key = "9fce61b89dea5c79c074b135dd1b31c679f5e2019b5a2a7a1cbd5d5ebf1adba3"
client = discord.Client()

bot = commands.Bot(command_prefix='$')

@bot.command()
async def test(ctx, arg1, arg2):
    print(arg1, arg2)
    await ctx.send('You passed {} and {}'.format(arg1, arg2))


my_secret = os.getenv('TOKEN')
client.run(my_secret)
