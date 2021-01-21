import discord,pymongo
from discord.ext import commands
import settings



class blackhole(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        # Re-define the bot object into the class.

    mongoclient = pymongo.MongoClient(settings.mongo_url)# Connect to MongoDB Server
    blackholedb = mongoclient["blackholedb"]
    blackholecol = blackholedb["channels"]

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def blackhole(self,ctx,channel: discord.TextChannel):
        # Blackhole allows server managers to dedicate a channel that auto-deletes all messages sent.

        # Check if the server already has a blackhole channel setup
        if (self.blackholedb.channels.count_documents({"serverid":ctx.guild.id}, limit = 1) != 0): 
            # Update the existing blackhole channel entry
            self.blackholecol.update_many({"serverid":ctx.guild.id},{"$set":{"channelid":channel.id}})
            await ctx.send(":white_check_mark: Blackhole channel updated for **" + ctx.guild.name + "**.")
        else:
            # If this is the server's first time blackhole setup, create a new entry.
            self.blackholecol.insert_one({"serverid":ctx.guild.id,"channelid":channel.id})
            await ctx.send(":white_check_mark: Blackhole channel set for **" + ctx.guild.name + "**.")
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def antiping(self,ctx):
        # Anti ping makes members refrain from abusing the blackhole channel by ghost pinging users and/or roles by exposing them. Messages are still not logged and privacy is preserved.
        query = {"serverid":ctx.guild.id}
        doc = self.blackholecol.find(query)
        for x in doc:
            # Check if there's an anti ping field
            try:
                status = x["antiping"]
            except:
                # If there is no field, add one and set it to on.
                self.blackholecol.update_many(query,{"$set":{"antiping":"on"}})
                await ctx.send(":white_check_mark: Anti-ping has been enabled in blackhole. Any and all pings will be automatically called out.")
                return
            # If there is already a field and anti ping is already enabled, disable it.
            if x["antiping"] == "on":
                self.blackholecol.update_many(query,{"$set":{"antiping":"off"}})
                await ctx.send(":white_check_mark: Anti-ping has been disabled in blackhole.")
                return
            # If there is already a field and anti ping is disabled, enable it.
            self.blackholecol.update_many(query,{"$set":{"antiping":"on"}})
            await ctx.send(":white_check_mark: Anti-ping has been enabled in blackhole. Any and all pings will be automatically called out.")
            return
        # If the server has no blackhole channel setup, abort and tell the user.
        await ctx.send(":warning: You don't have a blackhole channel setup yet.")


def setup(bot):
    bot.add_cog(blackhole(bot))