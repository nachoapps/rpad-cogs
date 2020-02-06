from .baduser import *

def setup(bot):
    print('baduser bot setup')
    n = BadUser(bot)
    bot.add_cog(n)
    print('done adding baduser bot')