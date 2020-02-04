from .padvision import *

def setup(bot):
    n = PadVision(bot)
    bot.add_cog(n)