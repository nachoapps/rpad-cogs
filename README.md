# rpad-cogs

Cogs developed for Miru Bot.

This codebase is a mess right now. I'm working on cleaning it up, promise =)

Code should adhere to the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

# Requirements

Cogs here depend on the following packages, which can be installed using `pip install <package name>` in the command prompt:

* PrettyTable
* backoff
* python-dateutil
* dill
* pytz
* ply
* numpy
* opencv-python
* pillow
* pymysql
* pypng
* aioodbc
* twython
* google-auth

Additionally, the cogs require `romkan` and `psutil`.

romkan: download zip file from https://github.com/tejstead/python-romkan and unzip it anywhere, open command prompt, cd to your python-romkan-master folder, and type `python setup.py install`

psutil: type `pip3 install psutil --upgrade` in command prompt

# Puzzle and Dragons

Most cogs here relate to the mobile game 'Puzzle and Dragons'. Data is sourced from the
PadHerder private API, which I have obtained permission to use for this bot.

I was asked not to share the details of how to access the API, so that code is not
checked in here.

| Cog        | Purpose                                                         |
| ---        | ---                                                             |
| damagecalc | Simple attack damage calculator                                 |
| padboard   | Converts board images to dawnglare board/solved board links     |
| padglobal  | Global PAD info commands                                        |
| padguide   | Utility classes relating to PadGuide data                       |
| padinfo    | Monster lookup and info display                                 |
| padrem     | Rare Egg Machine simulation                                     |
| padvision  | Utilities relating to PAD image scanning                        |
| profile    | Global user PAD profile storage and lookup                      |


# Admin/util cogs

Cogs that make server administration easier, do miscellaneous useful things, or
contain utility libraries.

| Cog            | Purpose                                                     |
| ---            | ---                                                         |
| baduser        | Tracks misbehaving users, other misc user tracking          |   
| calculator     | Replacement for the calculator cog that doesnt suck         |  
| fancysay       | Make the bot say special things                             |
| memes          | CustomCommands except role-limited                          |    
| rpadutils      | Utility library shared by many other libraries              |    
| sqlactivitylog | Archives messages in sqlite, allows for lookup              |    
| timecog        | Convert/print time in different timezones                   | 
| trutils        | Misc utilities intended for my usage only                   |
| twitter2       | Mirrors a twitter feed to a channel                         |


# Other/deprecated cogs

Cogs not intended for normal use, or superceded.

| Cog            | Purpose                                                     |
| ---            | ---                                                         |
| adminlog       | In-memory storage of user messages and lookup               |
| donations      | Tracks users who have donated for hosting fees              |
| supermod       | April fools joke, random moderator selection                |

