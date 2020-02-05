from .trutils import *

def setup(bot):
    print('trutils bot setup')
    n = TrUtils(bot)
    bot.add_listener(n.on_imgcopy_message, "on_message")
    bot.add_listener(n.on_imgcopy_edit_message, "on_message_edit")
    bot.add_listener(n.on_imgblacklist_message, "on_message")
    bot.add_listener(n.on_imgblacklist_edit_message, "on_message_edit")
    bot.add_listener(n.on_trackuser_update, "on_member_update")
    bot.add_cog(n)
    print('done adding trutils bot')