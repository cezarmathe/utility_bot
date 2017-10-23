

import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GSpread():
	def __init__(self):
		self.scope = ['https://spreadsheets.google.com/feeds']
		self.creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', self.scope)
		self.gclient = gspread.authorize(self.creds)
		self.database = self.gclient.open('discord_database')
		return 

class PollDatabase():
	def __init__(self):
		self.poll = GSpread()
		self.polls = self.poll.database.worksheet('Polls')
		return
	def value(self, x, y):
		return self.polls.cell(x,y).value
	def update(self, x, y, value):
		self.polls.update_cell(x, y, value)
		

class MemeDatabase():
	def __init__(self):
		self.meme = GSpread()
		self.memes = self.meme.database.worksheet('Memes')
		return
	def value(self, x, y):
		return self.memes.cell(x,y).value
	def update(self, x, y, value):
		self.memes.update_cell(x, y, value)


class CommandDatabase():
	def __init__(self):
		self.command = GSpread()
		self.commands = self.command.database.sheet1
		return
	def value(self, x, y):
		return self.commands.cell(x,y).value
	def update(self, x, y, value):
		self.commands.update_cell(x, y, value)


# https://github.com/burnash/gspread