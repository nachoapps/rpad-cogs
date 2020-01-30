from .modnotes import ModNotes

def setup(bot):
    n = ModNotes(bot)
    bot.add_cog(n)
