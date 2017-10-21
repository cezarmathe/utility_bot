

import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Database():

	scope = ['https://spreadsheets.google.com/feeds']
	creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	gclient = gspread.authorize(creds)
	polls = gclient.open("discord_database").sheet3
	memes = gclient.open("discord_database").sheet2

	def __init__(self):
		return

	def 