from .donations import Donations

def setup(bot):
    n = Donations(bot)
    bot.add_listener(n.checkCC, "on_message")
    bot.add_listener(n.check_insult, "on_message")
    bot.add_cog(n)
