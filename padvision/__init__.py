from .padvision import PadVision

def setup(bot):
    n = PadVision(bot)
    bot.add_cog(n)
