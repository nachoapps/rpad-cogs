from .padrem import PadRem

def setup(bot):
    print('padrem bot setup')
    n = PadRem(bot)
    bot.add_cog(n)
    bot.loop.create_task(n.reload_padrem())
    print('done adding padrem bot')
