import discord
from discord.ext import commands

class messaging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Re-define the bot object into the class.


    # Create a self-destructing message
    @commands.command(aliases=["timer","timed","destruct"])
    async def expire(self, ctx,*,parameters):
        splitted = parameters.split()# Split the parameters to check for a self-destruction time.
        timer = str(splitted[0])
        # If there's no specified time, set it to 5 seconds as a default.
        if timer.isnumeric() == False:
            timer = 5
        else:
            timer = int(splitted[0])# Take the first "argument" as the self-destructing timer.
            del splitted[0]
        # Delete the original message and replace it with an anonymous embed.
        await ctx.message.delete()
        embed=discord.Embed(title=":clock1: Self-Destructing Message from " + str(ctx.author.name), description=' '.join(splitted), color=0xff2600)
        embed.set_footer(text="Lifespan: " + str(timer) + " seconds")
        await ctx.send(embed=embed,delete_after=timer)# Send the anonymous embed and delete it after the specified or default self-destruction time.
    
    # Create a self-destructing anonymous message
    @commands.command(aliases=["anontimer","anontimed","anondestruct","anon-expire","anon-timer","anon-timed","anon-destruct"])
    async def anonexpire(self, ctx,*,parameters):
        splitted = parameters.split()# Split the parameters to check for a self-destruction time.
        timer = str(splitted[0])
        # If there's no specified time, set it to 5 seconds as a default.
        if timer.isnumeric() == False:
            timer = 5
        else:
            timer = int(splitted[0])# Take the first "argument" as the self-destructing timer.
            del splitted[0]
        # Delete the original message and replace it with an anonymous embed.
        await ctx.message.delete()
        embed=discord.Embed(title=":clock1: Self-Destructing Message from Anonymous", description=' '.join(splitted), color=0xff2600)
        embed.set_footer(text="Lifespan: " + str(timer) + " seconds")
        await ctx.send(embed=embed,delete_after=timer)# Send the anonymous embed and delete it after the specified or default self-destruction time.
    
    # Send an anonymous message.
    @commands.command()
    async def anon(self,ctx,*,msg):
        await ctx.message.delete()# Delete the original message and replace it with an anonymous embed
        embed = discord.Embed(title="Anonymous Message", description=msg, color=0xffffff)
        await ctx.send(embed=embed)# Send the anonymous embed
        
def setup(bot):
    bot.add_cog(messaging(bot))