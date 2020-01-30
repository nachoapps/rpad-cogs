from .statistics import Statistics

def setup(bot):
    if psutil is False:
        raise RuntimeError('psutil is not installed. Run `pip3 install psutil --upgrade` to use this cog.')
    else:
        check_folder()
        check_file()
        n = Statistics(bot)
        bot.add_cog(n)
