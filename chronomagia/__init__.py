from .chronomagia import ChronoMagia

def setup(bot):
    n = ChronoMagia(bot)
    bot.add_cog(n)
    bot.loop.create_task(n.reload_cm_task())
