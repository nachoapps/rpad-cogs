from .rpadutils import RpadUtils

def setup(bot):
    print('rpadutils setup')
    n = RpadUtils(bot)
    bot.add_cog(n)
