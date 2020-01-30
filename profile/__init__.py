from .profile import Profile

def setup(bot):
    print('profile bot setup')
    n = Profile(bot)
    bot.add_cog(n)
    print('done adding profile bot')
