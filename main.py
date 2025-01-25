import asyncio
from discord.ext import commands
import discord
import os
from constants import TOKEN , TODO_FILE

bot = commands.Bot(command_prefix="." , intents=discord.Intents.all())
bot.remove_command("help")



async def load():
    
    if not os.path.exists(TODO_FILE):
        with open(TODO_FILE , "w"):
            pass
    
    for filename in os.listdir("./cogs"):
        
        if filename.endswith(".py"):
            
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"{filename[:-3]} cog loaded")


async def main():
    async with bot:
        await load()
        await bot.start(TOKEN)
        
        
asyncio.run(main())