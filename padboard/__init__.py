from .padboard import PadBoard

def setup(bot):
    check_folder()
    check_file()
    n = PadBoard(bot)
    bot.add_listener(n.log_message, "on_message")
    bot.add_cog(n)
