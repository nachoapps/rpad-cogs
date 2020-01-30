from .fancysay import FancySay

def setup(bot):
    n = FancySay(bot)
    bot.add_cog(n)
