from .azurelane import AzureLane

def setup(bot):
    check_folders()
    check_files()
    n = AzureLane(bot)
    bot.add_cog(n)
    bot.loop.create_task(n.reload_al())
