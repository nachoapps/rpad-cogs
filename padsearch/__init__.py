from .padsearch import PadSearch

def setup(bot):
    n = PadSearch(bot)
    bot.add_cog(n)
