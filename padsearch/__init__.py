from .padsearch import *

def setup(bot):
    n = PadSearch(bot)
    bot.add_cog(n)