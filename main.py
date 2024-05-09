from typing import Final
import os

import discord
from discord.app_commands import commands
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responds import handle_respones
from discord.ext import commands
import commandss

load_dotenv()
TOKEN = 'api_key'

intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)

bot = commands.Bot(command_prefix='?', intents=intents)


@bot.command(name='hello')
async def hello(ctx):
    await commandss.hello(ctx)
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Yukina latency is around: {:.2f} ms'.format(bot.latency*1000))


@bot.command()
async def say(ctx, *what):
    await commandss.mp3(ctx, *what)


@bot.command()
async def repeat(ctx, *what):
    await commandss.get_text(ctx, *what)

@bot.command()
async def pick(ctx, first, second):
    await commandss.pick(ctx, first, second)

@bot.command()
async def ask(ctx, *what):
    await commandss.ask(ctx, *what)
@bot.command()
async def avatar(ctx, user: discord.Member):
    await commandss.avatar(ctx, user)
@bot.command()
async def svavatar(ctx, users: discord.Member):
    await commandss.svavatar(ctx, users)





'''async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = handle_respones(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)



@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')



@client.event
async def on_message(ctx,message : Message) -> None:
    if message.content == 'hello':
        await ctx.reply(f'Hello {message.author.mention}') '''


bot.run('api_key')
