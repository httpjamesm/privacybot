import discord,asyncio
from discord.ext import commands

class management(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        # Re-define the bot object into the class.

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def wipe(self,ctx):
        await ctx.send("Wiping channel in 15 seconds. Say `cancel` to abort.")
        def check(msg):# callback that waits for the user to say "cancel"
            if msg.author == ctx.author and msg.content.lower() == "cancel":
                return True
        try:# initiates callback
            msg = await ctx.bot.wait_for('message', check=check, timeout=15.0)
        except asyncio.TimeoutError:# if "cancel" is not received, wipe channel
            await ctx.channel.clone()
            await ctx.channel.delete()
        else:# abort if "cancel" is received
            await ctx.send("Operation aborted.",delete_after=15)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self,ctx,limit="0"):
        try:
            await ctx.channel.purge(limit=int(limit))
        except:
            await ctx.send(":warning: I couldn't purge any messages. Did you give me the correct permissions?")
            return
        await ctx.send("Purged **" + limit + "** messages!",delete_after=5)
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purgeuser(self,ctx,limit,target:discord.Member):
        def is_user(m):# Check to see if a message's author is the desired user to purge.
            return m.author == target
        # Purge messages that are only from the desired user.
        await ctx.channel.purge(limit=int(limit), check=is_user)
        await ctx.send("done")

"""@commands.command()
@commands.has_permissions(manage_guild=True)
async def setting(self,ctx,*,params=None):
    try:
        split_params = params.split()
        setting_name = str(params[0]).lower()
    except:
        await ctx.send(":warning: Invalid parameters!")
    if setting_name == "antipingttl" and is_integer(params[1]) == True:
        settings."""





def setup(bot):
    bot.add_cog(management(bot))