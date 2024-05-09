import discord
from discord.ext import commands
import elevenlabs
from elevenlabs.client import ElevenLabs
from discord.ext.commands import bot
from discord.ext import commands
from discord import Intents, Client, Message
from openai import OpenAI
import random
import pathlib
import textwrap

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


async def hello(ctx):
    await ctx.send('hello')


async def mp3(ctx, *user_input):
    user_input = ' '.join(user_input)
    client = ElevenLabs(
        api_key='api_key'
    )
    audio = client.generate(
        text=user_input,
        voice='Rachel',
        model='eleven_multilingual_v2'
    )
    elevenlabs.save(audio, 'audio.mp3')

    await ctx.send(file=discord.File(r'C:\Users\ASUS TUF GAMING A15\PycharmProjects\yukinamygirl\audio.mp3'))


async def get_text(ctx, *what):
    await ctx.send(' '.join(what))


async def pick(ctx, first, second):
    await ctx.send('My choice is: {} '.format(random.choice([first, second])))


async def ping(ctx):
    await ctx.send('Yukina latency is around {} ms'.format(round(bot.latency * 1000)))


async def avatar(ctx, user: discord.Member):
    await ctx.send(user.avatar)

async def svavatar(ctx, user: discord.Member):
    await ctx.send(user.display_avatar)



async def rule34(ctx,tag):
    r34py= rule34Py()

    tag.capitalize()
    r34py = r34py.random_post([tag])
    embed = discord.Embed(title=tag,description='Artist: '+ r34py.owner)
    embed.set_image(url=r34py.image)

    await ctx.send(embed=embed)
    




async def r34taglist(ctx):
    await ctx.send('https://rule34.xxx/index.php?page=tags&s=list')










'''async def ask(ctx, *what):
    openai_api: str='api_key'
    client = OpenAI(
        api_key=openai_api
    )
    user_input = ' '.join(what)
    respond = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": user_input}],
        stream=True,
    )'''
