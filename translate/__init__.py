from .translate import Translate

def setup(bot):
    n = Translate(bot)
    bot.add_listener(n.checkAutoTranslateJp, "on_message")
    bot.add_cog(n)
