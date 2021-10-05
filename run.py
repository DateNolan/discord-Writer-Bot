#!/usr/bin/env python3
import discord, json, lib
from bot import WriterBot
from discord.ext import commands
from discord_slash import SlashCommand

# Load the settings for initial setup
config = lib.get('./settings.json')

# Load the Bot object
status = discord.Game( 'Booting up...' )
bot = WriterBot(command_prefix=WriterBot.load_prefix, activity=status)
slash = SlashCommand(bot, sync_commands=True)

# Load all commands
bot.load_commands()

# Start the bot
bot.run(config.token)
