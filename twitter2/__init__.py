from .twitter2 import TwitterCog2

def setup(bot):
    print('twitter2 bot setup')
    check_folder()
    check_file()
    n = TwitterCog2(bot)
    loop = asyncio.get_event_loop()
    loop.create_task(n.connect())
    bot.add_cog(n)
    print('done adding twitter2 bot')
