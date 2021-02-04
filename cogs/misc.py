import discord
from discord.ext import commands
import datetime as dt

class misc(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        # Re-define the bot object into the class.
    
    @commands.command(aliases=["commands","cmds"])
    async def help(self,ctx):
        embed=discord.Embed(title="PrivacyBot Help", description="PrivacyBot is a bot that aims to bring more private communication to Discord communities.\n\nYou can invoke this at anytime using `!help`.", color=0x80ffff)
        embed.set_author(name=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=f"{ctx.author.avatar_url}")
        embed.set_thumbnail(url="https://privacybot.httpjames.space/assets/images/image01.png?v8be10201c")
        embed.add_field(name="Messaging", value="`!expire <time in s> <message>` - Send a self-destructing message. The default time (if not provided) is 10 seconds.\n`!anon-expire <time in s> <message>` - Send an anonymous self-destructing message. The default time (if not provided) is 10 seconds.\n`!anon <message>` - Send an anonymous message.", inline=False)
        embed.add_field(name="Shortcuts", value="Sending a message that begins with the following will invoke specific commands.\n\n`/<message>` - Send a 10 second self-destructing message.\n`//<message>` - Send an anonymous 10 second self-destructing message.", inline=False)
        embed.add_field(name="Blackhole", value="Blackholes are channels in which all sent messages are instantly deleted. Manage Channels is required for these commands.\n\n`!blackhole <#channel>` - Set a blackhole channel.\n`!antiping` - Enable/disable anti-ping.", inline=False)
        embed.add_field(name="Admin", value="Manage Messages or Manage Channels is required for these commands.\n\n`!purge <#>` - Purge a number of messages.\n`!purgeuser <#> <@mention>` - Scan through a number of messages and delete all messages from a user within.\n`!wipe` - Wipe an entire channel's messages.", inline=False)
        embed.set_footer(text="Made by http.james#6969")
        try:
            await ctx.author.send(embed=embed)
        except:
            await ctx.send(f":x: I couldn't send you a DM, {ctx.author.mention}.",delete_after=15)
            return
        await ctx.send(f":white_check_mark: Check your DMs, {ctx.author.mention}!",delete_after=15)

def setup(bot):
    bot.add_cog(misc(bot))