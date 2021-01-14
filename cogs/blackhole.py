import discord,pymongo
from discord.ext import commands
import settings



class blackhole(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    mongoclient = pymongo.MongoClient(settings.mongo_url)
    blackholedb = mongoclient["blackholedb"]
    blackholecol = blackholedb["channels"]
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def blackhole(self,ctx,channel: discord.TextChannel):
        if (self.blackholedb.channels.count_documents({"serverid":ctx.guild.id}, limit = 1) != 0):
            self.blackholecol.update_many({"serverid":ctx.guild.id},{"$set":{"channelid":channel.id}})
            await ctx.send(":white_check_mark: Blackhole channel updated for **" + ctx.guild.name + "**.")
            return
        self.blackholecol.insert_one({"serverid":ctx.guild.id,"channelid":channel.id})
        await ctx.send(":white_check_mark: Blackhole channel set for **" + ctx.guild.name + "**.")


def setup(bot):
    bot.add_cog(blackhole(bot))