import discord
import asyncio
import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials

@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('-------------')
    print('')

@client.event
async def on_message(message):
	if (message.content.startswith('!')):
		await client.send_message(message.channel, 'Succes')

client.run('MzUzNjE3MTc2NzkzNzEwNjEy.DIyULg.7J9_CWDYHr2PGeFJWmnPhRLV8BU')