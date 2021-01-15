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
        # Re-define the bot object into the class.

    # When the bot logs in, print bot details to console
    @commands.Cog.listener('on_ready')
    async def on_ready(self):
        print('[BOOT] Logged in at ' + str(dt.datetime.now()))
        await self.bot.change_presence(activity=discord.Game(name="!help"))
        print("[INFO] Username:",self.bot.user.name)
        print("[INFO] User ID:",self.bot.user.id)
    
    # When a message is detected, do X
    @commands.Cog.listener('on_message')
    async def on_message(self,message):
        if (blackholedb.channels.count_documents({ 'serverid':message.guild.id }, limit = 1) != 0):# Check if the server setup a blackhole channel
            doc = blackholecol.find({"serverid":message.guild.id})
            for x in doc:
                if message.channel.id == x["channelid"]:
                    # If the message is in the blackhole channel, delete it.
                    await message.delete()

        # Ephemeral Messaging Shortcuts
        splitted = list(message.content)
        if (message.content.startswith('/') and splitted[1] != "/"):
                await message.delete()
                del splitted[0]# Delete the shortcut invoker (/)
                # Delete the original message and send a self-destructing embed.
                embed=discord.Embed(title=":clock1: Self-Destructing Message from " + str(message.author.name), description=''.join(splitted), color=0xff2600)
                embed.set_footer(text="Lifespan: 10 seconds")
                await message.channel.send(embed=embed,delete_after=10)

        elif (message.content.startswith('//')):
                await message.delete()
                del splitted[:2]# Delete the shortcut invoker (//)
                # Delete the original message and send an anonymous self-destructing embed.
                embed=discord.Embed(title=":clock1: Self-Destructing Message from Anonymous", description=''.join(splitted), color=0xff2600)
                embed.set_footer(text="Lifespan: 10 seconds")
                await message.channel.send(embed=embed,delete_after=10)

def setup(bot):
    bot.add_cog(listeners(bot))