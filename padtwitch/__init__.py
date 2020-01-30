from .padtwitch import PadTwitch

def setup(bot):
    n = PadTwitch(bot)
    asyncio.get_event_loop().create_task(n.on_connect())
    bot.add_cog(n)
