from discord.ext import commands
import discord

class Dm(commands.Cog):
    
    def __init__(self, bot : commands.Bot):
        
        self.bot = bot
        
    
    @commands.command(name="dm")
    async def dm_command(
        self, ctx: commands.Context, member: commands.MemberConverter = None, *, message=None
    ):
        if member is None or message is None:
            embed = discord.Embed(
                title="DM Command Help",
                description="The `?dm` command sends a direct message to a specified user. "
                "You need to use it like this: `?dm <user> <message>`. "
                "Replace `<user>` with the user you want to message and `<message>` with the message you want to send.",
                color=0x00FF00,
            )
            return await ctx.send(embed=embed)

        if member == self.bot.user:
            return await ctx.send("I cannot message myself.")
        try:
            await member.send(f"{ctx.author.name} : {message}")

            await ctx.send("DM sent successfully.")
        except Exception as e:
            await ctx.send("Error in sending the message")

async def setup(bot : commands.Bot):

    await bot.add_cog(Dm(bot))