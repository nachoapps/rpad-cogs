from .automod2 import AutoMod2

def setup(bot):
    n = AutoMod2(bot)
    bot.add_listener(n.mod_message_images, "on_message")
    bot.add_listener(n.add_auto_emojis, "on_message")
    bot.add_listener(n.mod_message, "on_message")
    bot.add_listener(n.mod_message_edit, "on_message_edit")
    bot.add_listener(n.mod_message_watchdog, "on_message")
    bot.add_cog(n)
