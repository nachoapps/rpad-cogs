from .padbuilds import PadBuilds

def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(PadBuilds(bot))
