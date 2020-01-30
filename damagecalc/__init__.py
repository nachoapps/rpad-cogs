from .damagecalc import DamageCalc

def setup(bot):
    n = DamageCalc(bot)
    bot.add_cog(n)
