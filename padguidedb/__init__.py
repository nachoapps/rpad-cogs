from .padguidedb import PadGuideDb

def setup(bot):
    n = PadGuideDb(bot)
    bot.add_cog(n)
