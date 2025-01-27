import asyncio
from discord.ext import commands
import discord
import os
from constants import TOKEN

from mongodb.db_connect import main as connect

bot = commands.Bot(command_prefix="." , intents=discord.Intents.all())
bot.remove_command("help")



async def load():
    
    for filename in os.listdir("./cogs"):
        
        if filename.endswith(".py"):
            
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"{filename[:-3]} cog loaded")

async def run_bot():
    async with bot:
        await load()
        await bot.start(TOKEN)


async def main():
    await run_bot()
    collection = await connect()
    bot.db = collection

    
        
asyncio.run(main())