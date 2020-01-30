from .stickers import Stickers

def setup(bot):
    check_folders()
    check_files()
    n = Stickers(bot)
    bot.add_listener(n.checkCC, "on_message")
    bot.add_cog(n)
