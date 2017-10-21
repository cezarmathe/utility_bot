

import discord
import asyncio
import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import constants as constants
import database


client = discord.Client()	
polls = PollDatabase() 

@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('-------------')
    print('')

@client.event
async def on_message(message):
	if (message.content.startswith('!'):
		await cliend.send_message(message.channel, polls.value(constants.START, constants.INDEX))

		







client.run('MzUzNjE3MTc2NzkzNzEwNjEy.DIyULg.7J9_CWDYHr2PGeFJWmnPhRLV8BU')



# https://discordapp.com/oauth2/authorize?client_id=353617176793710612&scope=bot&permissions=0x00000008