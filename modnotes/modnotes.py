"""
Utilities for managing moderator notes about users.
"""

import discord
from discord.ext import commands

from __main__ import send_cmd_help
from __main__ import settings

from redbot import rpadutils
from redbot.rpadutils import CogSettings
from redbot.utils import checks
from redbot.utils.chat_formatting import *


class ModNotes:
    def __init__(self, bot):
        self.conf = Config.get_conf(self, identifier=70070735, force_registration=True)

        self.bot = bot
        self.settings = ModNotesSettings("modnotes")

    @commands.group(, aliases=["usernote"])
    @checks.mod_or_permissions(manage_guild=True)
    async def usernotes(self, context):
        """Moderator notes for users.

        This module allows you to create notes to share between moderators.
        """
        if context.invoked_subcommand is None:
            await send_cmd_help(context)

    @usernotes.command(name="print")
    @checks.mod_or_permissions(manage_guild=True)
    async def _print(self, ctx, user: discord.User):
        """Print the notes for a user."""
        notes = self.settings.getNotesForUser(ctx.message.guild.id, user.id)
        if not notes:
            await ctx.send(box('No notes for {}'.format(user.name)))
            return

        for idx, note in enumerate(notes):
            await ctx.send(inline('Note {} of {}:'.format(idx + 1, len(notes))))
            await ctx.send(box(note))

    @usernotes.command()
    @checks.mod_or_permissions(manage_guild=True)
    async def add(self, ctx, user: discord.User, *, note_text: str):
        """Add a note to a user."""
        timestamp = str(ctx.message.created_at)[:-7]
        msg = 'Added by {} ({}): {}'.format(ctx.message.author.name, timestamp, note_text)
        server_id = ctx.message.guild.id
        notes = self.settings.addNoteForUser(server_id, user.id, msg)
        await ctx.send(inline('Done. User {} now has {} notes'.format(user.name, len(notes))))

    @usernotes.command()
    @checks.mod_or_permissions(manage_guild=True)
    async def delete(self, ctx, user: discord.User, note_num: int):
        """Delete a specific note for a user."""
        notes = self.settings.getNotesForUser(ctx.message.guild.id, user.id)
        if len(notes) < note_num:
            await ctx.send(box('Note not found for {}'.format(user.name)))
            return

        note = notes[note_num - 1]
        notes.remove(note)
        self.settings.setNotesForUser(ctx.message.guild.id, user.id, notes)
        await ctx.send(inline('Removed note {}. User has {} remaining.'.format(note_num, len(notes))))
        await ctx.send(box(note))

    @usernotes.command()
    @checks.mod_or_permissions(manage_guild=True)
    async def list(self, ctx):
        """Lists all users and note counts for the server."""
        user_notes = self.settings.getUserNotes(ctx.message.guild.id)
        msg = 'Notes for {} users'.format(len(user_notes))
        for user_id, notes in user_notes.items():
            user = ctx.message.guild.get_member(int(user_id))
            user_text = '{} ({})'.format(user.name, user.id) if user else user_id
            msg += '\n\t{} : {}'.format(len(notes), user_text)

        for page in pagify(msg):
            await ctx.send(box(page))



class ModNotesSettings(CogSettings):
    def make_default_settings(self):
        config = {
            'servers': {}
        }
        return config

    def servers(self):
        return self.bot_settings['servers']

    def getServer(self, server_id):
        servers = self.servers()
        if server_id not in servers:
            servers[server_id] = {}
        return servers[server_id]

    def getUserNotes(self, server_id):
        server = self.getServer(server_id)
        key = 'user_notes'
        if key not in server:
            server[key] = {}
        return server[key]

    def getNotesForUser(self, server_id, user_id):
        user_notes = self.getUserNotes(server_id)
        return user_notes.get(user_id, [])

    def setNotesForUser(self, server_id, user_id, notes):
        user_notes = self.getUserNotes(server_id)

        if notes:
            user_notes[user_id] = notes
        else:
            user_notes.pop(user_id, None)
        self.save_settings()
        return notes

    def addNoteForUser(self, server_id, user_id, note: str):
        notes = self.getNotesForUser(server_id, user_id)
        notes.append(note)
        self.setNotesForUser(server_id, user_id, notes)
        return notes
