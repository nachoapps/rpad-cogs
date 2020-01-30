from .schoolidol import SchoolIdol

def setup(bot):
    check_folders()
    check_files()
    n = SchoolIdol(bot)
    bot.add_cog(n)
    bot.loop.create_task(n.reload_sif())
