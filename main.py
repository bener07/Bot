from discord.ext import commands
import discord
import os
from Crypto import crypto

client = discord.Client()
api_key = os.getenv('API_KEY')

bot = commands.Bot(command_prefix='$')


@bot.command(name='price')
async def hi(ctx, symbol, exchange='USD', limit='1', code=False, low_info=False):
    await ctx.send(crypto(api_key, symbol, exchange, limit, code, low_info).price())


@bot.command(name='mining')
async def hi(ctx, symbol, exchange='USD', limit='1', code=False, low_info=False):
    await ctx.send(crypto(api_key, symbol, exchange, limit, code, low_info).mining_currency())


@bot.command(name='top')
async def hi(ctx, symbol, exchange='USD', limit='1', code=False, low_info=False):
    await ctx.send(crypto(api_key, symbol, exchange, limit, code, low_info).top())


@bot.command(name='social')
async def hi(ctx, symbol, exchange='USD', limit='1', code=False, low_info=False):
    await ctx.send(crypto(api_key, symbol, exchange, limit, code, low_info).social())


bot.run(os.getenv('TOKEN'))
