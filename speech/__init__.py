from .speech import Speech

def setup(bot):
    n = Speech(bot)
    bot.add_cog(n)
