from .memes import *

def setup(bot):
    check_folders()
    check_files()
    n = Memes(bot)
    bot.add_listener(n.checkCC, "on_message")
    bot.add_cog(n)