from .channelmod import ChannelMod

def setup(bot):
    n = ChannelMod(bot)
    bot.add_cog(n)
    bot.add_listener(n.log_channel_activity_check, "on_message")
    bot.loop.create_task(n.channel_inactivity_monitor())
    bot.add_listener(n.mirror_msg_new, "on_message")
    bot.add_listener(n.mirror_msg_edit, "on_message_edit")
    bot.add_listener(n.mirror_msg_delete, "on_message_delete")
    bot.add_listener(n.mirror_reaction_add, "on_reaction_add")
    bot.add_listener(n.mirror_reaction_remove, "on_reaction_remove")
