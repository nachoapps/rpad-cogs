from .baduser import BadUser

def setup(bot):
    print('baduser bot setup')
    n = BadUser(bot)
    bot.add_listener(n.mod_message, "on_message")
    bot.add_listener(n.mod_ban, "on_member_ban")
    bot.add_listener(n.check_punishment, "on_member_update")
    bot.add_listener(n.mod_user_join, "on_member_join")
    bot.add_listener(n.mod_user_left, "on_member_remove")
    bot.add_cog(n)
    print('done adding baduser bot')
