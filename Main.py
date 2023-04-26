import asyncio

import discord
from discord.ext import commands
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    try:
        await bot.load_extension('CommandsCog')
    except Exception as e:
        print(f'Failed to load extension MusicCog: {e}')


async def main():
    token = os.getenv('DISCORD')
    await bot.login(token)
    await bot.connect()
    # Load the music_cog extension


if __name__ == '__main__':
    asyncio.run(main())
