

import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GSpread():
	scope = ['https://spreadsheets.google.com/feeds']
	creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	gclient = gspread.authorize(creds)
	def __init__():
		return

class PollDatabase():
	poll = GSpread()
	polls = poll.gclient.open("discord_database").sheet3
	memes = gclient.open("discord_database").sheet2
	def __init__():
		return
	def value(x, y):
		return polls.cell(x, y).value

class MemeDatabase():
	meme = GSpread()
	polls = meme.gclient.open("discord_database").sheet3
	memes = gclient.open("discord_database").sheet2
	def __init__():
		return
	def value(x, y):
		return memes.cell(x, y).value


