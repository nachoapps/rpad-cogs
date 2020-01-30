from .rpadutils import *

def setup(bot):
    print('rpadutils setup')
    n = RpadUtils(bot)
    bot.add_cog(n)

__all__ = list(globals())