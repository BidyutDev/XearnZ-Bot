from discord.ext import commands , tasks
from itertools import cycle
import discord

class Ping(commands.Cog):
    
    
    
    def __init__(self, bot : commands.Bot):
        self.bot = bot
        self.status = cycle(["with you" , "with myself now"])
        
    @tasks.loop(seconds=30)
    async def change_status(self):
        await self.bot.change_presence(activity=discord.Game(next(self.status)))
    
    @commands.Cog.listener()
    async def on_ready(self):
        
        print(f"Yo i am ready {self.bot.user.name}")
        await self.change_status.start()
        
    @commands.command()
    async def ping(self , ctx : commands.Context):

        await ctx.send(f"{ctx.author.mention} Hello")


        
async def setup(bot : commands.Bot):
    
    await bot.add_cog(Ping(bot))

