

import discord
import asyncio
import objects as obj
import database as database
import constants as constants
import variables as variables
import utilities as utils
import basic_commands as commands
import classes as classes


class Command():
	# Handles a specific command
	def __init__(self, data_holder : classes.CommandDataHolder, custom = False):
		self.data_holder = data_holder
		self.custom = custom
		return
	async def run_custom(self):
		return
	async def run(self):
		if (self.custom):
			await self.run_custom()
			return
		if (self.data_holder.name == 'help'):
			await commands.help(self.data_holder)
			return
		if (self.data_holder.name == 'commands'):
			await commands.commands(self.data_holder)
			return
		if (self.data_holder.name == 'errors'):
			await commands.errors(self.data_holder)
			return
		if (self.data_holder.name == 'say'):
			await commands.say(self.data_holder)
			return


class BasicChecker():
	# Checks a message for a command
	def __init__(self, data : classes.Message):
		self.data = data
		self.name = data.args_array[0]
	async def succes(self):
		x = classes.CommandDataHolder(self.name, self.data.args_array, self.data.args_text, self.data.channel, self.data.author)
		y = Command(x)
		await y.run()
	async def check(self):
		if (self.name == 'help'):
			await self.succes()
			return True
		if (self.name == 'commands'):
			await self.succes()
			return True
		if (self.name == 'errors'):
			await self.succes()
			return True
		if (self.name == 'say'):
			await self.succes()
			return True
		return False
	

class CustomChecker():
	# Checks a message for a custom command
	def __init__(self, data : classes.Message):
		self.channel = data.channel
		self.name = data.args_array[0]
		self.database = classes.COMMANDS
		self.max = int(self.database.value(1,1)) + 1
		return
	async def check(self):
		for i in range(self.max):
			if (self.name == self.database.value(constants.COM_START + i, constants.COM_ID)):
				return i
		return False

	async def do(self, id):
		sender = classes.Sender(self.channel, self.database.value(id + constants.COM_START, constants.COM_TEXT))
		await sender.send()
		return


