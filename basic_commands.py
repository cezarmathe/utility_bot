

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
	embedder = classes.Embedder(data_holder.channel, 'Help section', 'This is the help section of this bot.', 0x000000)
	embedder.add_field('Prefix', 'The prefix for using this bot is !')
	embedder.add_field('Command list' , 'For a list of commands, type !commands')
	embedder.add_field('MEMEZ', 'MMEEMMEEZZ')
	await embedder.send()
	return


async def commands(data_holder : classes.CommandDataHolder):
	return


async def errors(data_holder : classes.CommandDataHolder):
	return


async def say(data_holder : classes.CommandDataHolder):
	text = data_holder.args_text.upper()
	sender = classes.Sender(data_holder.channel, text)
	await sender.send()
	return