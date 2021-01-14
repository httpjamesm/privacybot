import discord
from discord.ext import commands

class messaging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    def is_number(self,s):
        try:
            int(s)
            return True
        except ValueError:
            return False
    @commands.command(aliases=["timer","timed","destruct"])
    async def expire(self, ctx,*,parameters):
        splitted = parameters.split()
        integer_detected = self.is_number(str(splitted[0]))
        if integer_detected == False:
            timer = 5
        else:
            timer = int(splitted[0])
            del splitted[0]
        await ctx.message.delete()
        embed=discord.Embed(title=":clock1: Self-Destructing Message from " + str(ctx.author.name), description=' '.join(splitted), color=0xff2600)
        embed.set_footer(text="Lifespan: " + str(timer) + " seconds")
        await ctx.send(embed=embed,delete_after=timer)
    @commands.command(aliases=["anontimer","anontimed","anondestruct","anon-expire","anon-timer","anon-timed","anon-destruct"])
    async def anonexpire(self, ctx,*,parameters):
        splitted = parameters.split()
        integer_detected = self.is_number(str(splitted[0]))
        if integer_detected == False:
            timer = 5
        else:
            timer = int(splitted[0])
            del splitted[0]
        await ctx.message.delete()
        embed=discord.Embed(title=":clock1: Self-Destructing Message from Anonymous", description=' '.join(splitted), color=0xff2600)
        embed.set_footer(text="Lifespan: " + str(timer) + " seconds")
        await ctx.send(embed=embed,delete_after=timer)
    @commands.command()
    async def anon(self,ctx,*,msg):
        await ctx.message.delete()
        embed = discord.Embed(title="Anonymous Message", description=msg, color=0xffffff)
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(messaging(bot))