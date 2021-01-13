import discord,json
from discord.ext import commands

import sys, traceback

try:
    with open('config.json', 'r') as config_file:
        configdata = json.load(config_file)
        token = configdata["token"]
        prefix = configdata["prefix"]
except:
    print("No config.json file found! Exiting application now.")
    exit()

initial_extensions = [
    'cogs.messaging',
    'cogs.management',
    'cogs.misc'
]

bot = commands.Bot(command_prefix=prefix)
@bot.event
async def on_message(message):
    splitted = list(message.content)
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
        await bot.process_commands(message)


@bot.command()
@commands.cooldown(1,30,commands.BucketType.guild)
async def ping(ctx):
    await ctx.send('Pong! {0} seconds.'.format(round(bot.latency, 5)))
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)
@bot.event
async def on_ready():
    print('Logged in')
    await bot.change_presence(activity=discord.Game(name="!help"))
    print("Username: ",bot.user.name)
    print("Userid: ",bot.user.id)
bot.run(token)