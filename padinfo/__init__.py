from .padinfo import PadInfo

def setup(bot):
    print('padinfo bot setup')
    n = PadInfo(bot)
    bot.add_cog(n)
    bot.loop.create_task(n.reload_nicknames())
    print('done adding padinfo bot')
