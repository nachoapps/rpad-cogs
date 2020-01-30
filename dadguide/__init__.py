from .dadguide import Dadguide

def setup(bot):
    n = Dadguide(bot)
    bot.add_cog(n)
    n.register_tasks()
