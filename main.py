import discord,json
from discord.ext import commands

import sys, traceback

try:
    with open('config.json', 'r') as config_file:
        configdata = json.load(config_file)
        token = configdata["token"]
except:
    print("No config.json file found! Exiting application now.")
    exit()

initial_extensions = [
    'cogs.messaging',
    'cogs.management',
    'cogs.misc'
]

bot = commands.Bot(command_prefix=['!'])

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