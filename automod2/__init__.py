from .automod2 import *

def setup(bot):
    n = AutoMod2(bot)
    bot.add_cog(n)