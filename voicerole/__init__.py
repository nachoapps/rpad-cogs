from .voicerole import VoiceRole

def setup(bot):
    n = VoiceRole(bot)
    bot.add_listener(n._on_voice_state_update, 'on_voice_state_update')
    bot.add_cog(n)