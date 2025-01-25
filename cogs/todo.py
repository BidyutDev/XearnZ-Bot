from discord.ext import commands
from constants import TODO_FILE
import os
import asyncio
from discord import Message
import aiofiles
import json

class Todo(commands.Cog):
    
    def __init__(self , bot : commands.Bot):
        self.bot = bot
        
        
    @staticmethod
    async def get_todos():
        try:
            async with aiofiles.open(TODO_FILE ,"r")  as  f:
                content = await f.read()

                req = json.loads(content)
                return req
            
        except Exception as e:
            print(f"Error reading TODO file: {e}")
            return []

    @staticmethod
    async def get_user_todos(user_id):
        todos = await Todo.get_todos()

        for todo in todos:
            if todo["user_id"] == user_id:
                return todo
            
        return []
                
        
    @staticmethod
    async def add_todos(data):
        try:
            async with aiofiles.open(TODO_FILE , "w") as f:
                await f.write(json.dumps(data , indent=4))
                return True
        except Exception as e:
            print(f"Error saving TODOS : {e}")
            return False
    
    @commands.command(aliases=["tadd"])
    async def todo_add(self , ctx : commands.Context , * , task : str):
        todos = await Todo.get_todos()
        
        user_todos = await Todo.get_user_todos(str(ctx.author.id))

        if user_todos:
            user_todos["todos"].append({"task" : task , "completed" : False})
            
            for user in todos:
                if user["user_id"] == user_todos["user_id"]:
                    todos.remove(user)
                    todos.append(user_todos)
            
        else:
            todos.append({"user_id" : str(ctx.author.id) , "todos" : [{"task" : task , "completed" : False}]})
            
        
        await Todo.add_todos(todos)
        await ctx.send(f"Todo is added")
        
    @commands.command(aliases=["tshow"])
    async def show_todos(self, ctx: commands.Context):
        user_todos = await Todo.get_user_todos(str(ctx.author.id))

        if not user_todos:
            await ctx.send(f"No todos found for user {ctx.author.name}.")
            return
        
        table = "```"
        table += "{:<10} | {:<60} | {:<10}\n".format("S.No", "Task", "Completed")
        table += "-"*90 + "\n"

        for idx, todo in enumerate(user_todos["todos"], start=1):
            completed = "Yes" if todo['completed'] else "No"
            table += "{:<10} | {:<60} | {:<10}\n".format(idx, todo['task'], completed)

        table += "```"

        await ctx.send(f"**Todos for User {ctx.author.name}:**\n{table}")
        
    
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
            os.remove(TODO_FILE)
            await ctx.send(f"Todos have been deleted : {ctx.author.id}")
        
        except asyncio.TimeoutError:
            
            await ctx.send(f"{ctx.author.mention} Failed to delete due to timeout")
        

    @clear_todos.error
    async def clear_todos_error(self , ctx : commands.Context , error : commands.CommandError):
        
        if isinstance(error , commands.MissingPermissions):
            await ctx.send("You need administrator permissions to clear todos")

    
async def setup(bot : commands.Bot):
    await bot.add_cog(Todo(bot))
