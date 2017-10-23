

import discord
import asyncio
import objects as obj
import database as database
import constants as constants
import variables as variables
import classes as classes


# async def say(message : discord.message, text):
# 	await handlers.message_sender(message, text.upper())

async def help(data_holder : classes.CommandDataHolder):
	embedder = classes.Embedder(data_holder.channel, 'Help section', 'This is the help section of this bot.', constants.RANDCOLOR)
	embedder.add_field('Prefix', 'The prefix for using this bot is !')
	embedder.add_field('Command list' , 'For a list of commands, type !commands')
	embedder.add_field('MEMEZ', 'MMEEMMEEZZ')
	await embedder.send()
	return


async def commands(data_holder : classes.CommandDataHolder):
	embedder = classes.Embedder(data_holder.channel, 'Commands', 'This is a list of the available commands.', constants.RANDCOLOR)
	embedder.add_field('!help', 'Display the help section', True)
	embedder.add_field('!commands', 'Display this list', True)
	embedder.add_field('!errors', 'Display a list of possible errors that this bot could signal', True)
	embedder.add_field('!say', 'The bot says with uppercase letter what you wrote')
	await embedder.send()
	return


async def errors(data_holder : classes.CommandDataHolder):
	embedder = classes.Embedder(data_holder.channel, 'Errors', 'This is a list of errors that the bot could signal.', constants.RANDCOLOR)
	embedder.add_field('0x00', 'Unknown error', True)
	embedder.add_field('0x01', 'The bot encountered a situation where it had to send an empty message.')
	await embedder.send()
	return


async def say(data_holder : classes.CommandDataHolder):
	text = data_holder.args_text.upper()
	sender = classes.Sender(data_holder.channel, text)
	await sender.send()
	return