
import discord
import utilities as utils
import objects as obj
import database as database


POLLS = database.PollDatabase() 
MEMES = database.MemeDatabase()
COMMANDS = database.CommandDatabase()

class CommandDataHolder():
	# Holds data for commands
	def __init__(self, name, args_array, args_text, channel, author):
		self.name = name
		self.args_array = args_array
		self.args_text = args_text
		self.channel = channel
		self.author = author
		return

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
			# raise e
			errhandler = ErrorHandler(self.channel, False, '0x01')
			await errhandler.handle()

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
	def __init__(self, message : discord.message):
		self.message = message
		self.channel = message.channel
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

