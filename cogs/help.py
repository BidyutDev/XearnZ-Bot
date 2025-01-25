import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="help")
    async def help_command(self, ctx: commands.Context):
       
        embed = discord.Embed(
            title="Bot Help",
            description=f"**Owner** : <@1288870270664179815>\nBelow are the **commands** you can use:",
            color=discord.Color.blue()  
        )
        
        
        embed.add_field(
            name="`!tshow`",
            value="Displays all the to-dos for the user, showing whether each is completed or not.",
            inline=False
        )

        embed.add_field(
            name="`!tadd <task>`",
            value="Adds a new to-do for the user.",
            inline=False
        )
        
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
        guild_icon = ctx.author.guild.icon
        
        if guild_icon:
            embed.set_thumbnail(guild_icon.url)
            
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot))
