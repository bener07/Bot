from discord.ext import commands
import discord
import os
from Crypto import crypto

client = discord.Client()
api_key = '9fce61b89dea5c79c074b135dd1b31c679f5e2019b5a2a7a1cbd5d5ebf1adba3'

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
