from discord.ext import commands
import asyncio
from discord import Message


class Todo(commands.Cog):
    
    def __init__(self , bot : commands.Bot):
        self.bot = bot
        
        
    
    @commands.command(aliases=[""])
    async def mark_as_complete(self , ctx : commands.Context):
        pass

        
    @commands.command(aliases=["tclear"])
    @commands.has_permissions(administrator=True)
    async def clear_todos(self , ctx : commands.Context):
        await ctx.send(f"{ctx.author.mention} Warning : This will delete all the todos . Type DELETE to confirm it.")

        def check(message : Message):
            return message.author == ctx.author and message.content == "DELETE"
        try:
            await self.bot.wait_for('message', check=check , timeout=10)
            await ctx.send(f"Todos have been deleted : {ctx.author.id}")
        
        except asyncio.TimeoutError:
            
            await ctx.send(f"{ctx.author.mention} Failed to delete due to timeout")
        

    @clear_todos.error
    async def clear_todos_error(self , ctx : commands.Context , error : commands.CommandError):
        
        if isinstance(error , commands.MissingPermissions):
            await ctx.send("You need administrator permissions to clear todos")

    
async def setup(bot : commands.Bot):
    await bot.add_cog(Todo(bot))
