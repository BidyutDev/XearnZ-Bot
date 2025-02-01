from discord.ext import commands


class Purge(commands.Cog):
    
    def __init__(self , bot : commands.Bot):

        self.bot = bot


    @commands.has_permissions(administrator=True)
    @commands.command(name="purge")
    async def purge_command(self , ctx : commands.Context  , amount : int):
        print(ctx.author.id , type(ctx.author.id))
        if ctx.author.id != 1288870270664179815:

            return await ctx.send("Aborted")


        await ctx.channel.purge(limit=amount+1)
        await ctx.send(f"{amount} messages are deleted succesfully" , ephemeral=True)
    
    @purge_command.error
    async def handle_purge_error(self , ctx : commands.Context , err : commands.CommandError):
        
        await ctx.send("You dont have required permissions to purge messages")
    
async def setup(bot : commands.Bot):

    await bot.add_cog(Purge(bot))
    