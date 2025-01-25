from discord.ext import commands
import discord
import wavelink
from constants import WAVELINK_PASSWORD , WAVELINK_URI

class Music(commands.Cog):

    def __init__(self , bot : commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.loop.create_task(self.node_connect())
        
    
    async def node_connect(self):

        await self.bot.wait_until_ready()
        nodes = [wavelink.Node(uri=WAVELINK_URI,password=WAVELINK_PASSWORD)]
        
        await wavelink.Pool.connect(nodes=nodes , client=self.bot , cache_capacity=None)

    async def on_wavelink_node_ready(node : wavelink.Node):
        print(f"Node {node.identifier} is ready")
    
    
    @commands.command(aliases=["play"])
    async def play_song(self , ctx : commands.Context , * , search : str):
        
        if not ctx.author.voice:
            await ctx.send("You need to join a voice channel first!")
            return

        if not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player = ctx.voice_client

        tracks = await wavelink.Playable.search(search)

        if not tracks:
            await ctx.send("No results found.")
            return
        
        
        print(tracks)
        track = tracks[0]

        try:
            
            await vc.play(track)
            await ctx.send(f"Now playing: {track.title}")
            
        except Exception as e:
            await ctx.send(f"Error while trying to play the track: {str(e)}")
            print(f"Error while trying to play the track: {str(e)}")


async def setup(bot : commands.Bot):

    await bot.add_cog(Music(bot))