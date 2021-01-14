import discord,pymongo
import datetime as dt
from discord.ext import commands
import settings

mongoclient = pymongo.MongoClient(settings.mongo_url)
blackholedb = mongoclient["blackholedb"]
blackholecol = blackholedb["channels"]



class listeners(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener('on_ready')
    async def on_ready(self):
        print('[BOOT] Logged in at ' + str(dt.datetime.now()))
        await self.bot.change_presence(activity=discord.Game(name="!help"))
        print("[INFO] Username:",self.bot.user.name)
        print("[INFO] User ID:",self.bot.user.id)
    
    @commands.Cog.listener('on_message')
    async def on_message(self,message):
        splitted = list(message.content)
        if (blackholedb.channels.count_documents({ 'serverid':message.guild.id }, limit = 1) != 0):
            doc = blackholecol.find({"serverid":message.guild.id})
            for x in doc:
                if message.channel.id == x["channelid"]:
                    await message.delete()
                    return
        if (message.content.startswith('/') and splitted[1] != "/"):
                await message.delete()
                del splitted[0]
                embed=discord.Embed(title=":clock1: Self-Destructing Message from " + str(message.author.name), description=''.join(splitted), color=0xff2600)
                embed.set_footer(text="Lifespan: 10 seconds")
                await message.channel.send(embed=embed,delete_after=10)
        elif (message.content.startswith('//')):
                await message.delete()
                del splitted[:2]
                embed=discord.Embed(title=":clock1: Self-Destructing Message from Anonymous", description=''.join(splitted), color=0xff2600)
                embed.set_footer(text="Lifespan: 10 seconds")
                await message.channel.send(embed=embed,delete_after=10)
        else:
            await self.bot.process_commands(message)




def setup(bot):
    bot.add_cog(listeners(bot))