from .sqlactivitylog import SqlActivityLogger

def setup(bot):
    check_folders()
    check_files()
    n = SqlActivityLogger(bot)
    bot.add_cog(n)
