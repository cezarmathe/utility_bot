

import discord
import asyncio
import objects as obj
import database as database
import constants as constants
import variables as variables
import utilities as utils
import basic_commands as commands


class ErrorHandler():
	# Handles errors
	def __init__(self, channel, silent = True, errcode = '0x00'):
		self.errcode = errcode
		self.silent = silent
		self.channel = channel
		return
	async def handle(self):
		if (self.silent):
			return True
		if (self.errcode == '0x00'):
			await obj.client.send_message(self.channel, 'There was an unknown error.')
			return True
		if (self.errcode == '0x01'):
			await obj.client.send_message(self.channel, 'The bot encountered an error while sending a message.')
			return True
		return True


class Message():
	# Contains info about a received message
	def __init__(self, message : discord.message, channel):
		self.message = message
		self.channel = channel
		self.content = message.content
		self.author = message.author
		self.args_array = utils.args_array(message.content)
		self.args_text = utils.args_text(message.content)
		return
	def get_message(self):
		return self.message
	def get_channel(self):
		return self.channel
	def get_content(self):
		return self.content
	def get_author(self):
		return self.author
	def get_array(self):
		return self.args_array
	def get_text(self):
		return self.args_text


class Sender():
	# Sends messages
	def __init__(self, channel, content):
		self.channel = channel
		self.content = content
		return
	async def send(self):
		try:
			await obj.client.send_message(self.channel, self.content)
		except Exception as e:
			errhandler = ErrorHandler(self.channel, False, '0x01')
			await errhandler.handle()


class Channel():
	def __init__(self, channel):
		self.channel = channel
		return
	def get_channel(self):
		return self.channel


class Embedder():
	# Sends embedded messages
	def __init__(self, channel, title, description, color = 0x000000):
		self.channel = channel
		self.embed = discord.Embed(title = title, description = description, color = color)
		return
	def add_field(self, name, value, inline = False):
		self.embed.add_field(name = name, value = value, inline = inline)
		return
	async def send(self):
		await obj.client.send_message(self.channel, embed=self.embed)
		return



class Command():
	# Handles a specific command
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