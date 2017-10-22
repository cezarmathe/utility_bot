

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
		x = classes.CommandDataHolder(self.name, self.data.args_array, self.data.args_text, self.data.channel)
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
	def __init__(self):
		return


# async def message_handler(message: discord.message):
# 	args_array = utils.args_array(message.content[0:])
# 	# await commands.say(message.channel, args_array[0])
# 	# return True
# 	if (basic_command_checker(args_array[0])):
# 		args_text = utils.args_text(message.content[0:])
# 		await basic_command_handler(message, args_array[0], args_array, args_text)
# 		return True

# 	return False

# def basic_command_checker(command):
# 	if (command == 'help'):
# 		return True
# 	if (command == 'commands'):
# 		return True
# 	if (command == 'say'):
# 		return True
# 	return False

# async def basic_command_handler(message : discord.message, command, args_array, args_text):
# 	if (command == 'say'):
# 		await commands.say(message.channel, args_text[4:])
# 		return True
# 	return False

# async def message_sender(message : discord.message, payload):
# 	try:
# 		await obj.client.send_message(message, payload)
# 	except Exception as e:
# 		# await error_handler(message, 0)
# 		# return True
# 		handler = ErrorHandler(message, False, '0x01')
# 		await handler.handle()
# 	else:
# 		return True
		


# async def error_handler(message : discord.message, errcode)	:
# 	if (errcode == 0):
# 		await obj.client.send_message(message, 'You cannot send an empty message.')
# 		return True




	# try:
	# 	await obj.client.send_message(message.channel, '123')
	# except Exception as e:
	# 	await obj.client.send_message(message.channel, e)
	# else:
	# 	await obj.client.send_message(message.channel, 'succesfully ran through try..except..else')
	# return