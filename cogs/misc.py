import discord
from discord.ext import commands
bot = commands.Bot(command_prefix=['!'])

class misc(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

        #await ctx.send('Pong! {0} seconds.'.format(round(commands.Bot.latency, 5)))
    
def setup(bot):
    bot.add_cog(misc(bot))