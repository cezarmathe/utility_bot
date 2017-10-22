

import discord
import asyncio
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import constants as constants
import variables as variables
import database as database
import handlers as handlers
import objects as obj


POLLS = database.PollDatabase() 
MEMES = database.MemeDatabase()

@obj.client.event
async def on_ready():
    print('Logged in as:')
    print(obj.client.user.name)
    print(obj.client.user.id)
    print('-------------')
    print('')
    await obj.client.change_presence(game=discord.Game(name='Valoare mare'))

@obj.client.event
async def on_message(message):
	chanel = handlers.Channel(message.channel)

	if (message.content.startswith(constants.PREFIX)):
		 # handled = await handlers.message_handler(message)
		 # if (handled):
		 # 	return
		 # else:
		 # 	await obj.client.send_message(message.channel, 'There was an error handling your message.')
		 x = handlers.Message(message, chanel.get_channel())
		 y = handlers.Sender(chanel.get_channel(), 'test message ' + x.args_text)
		 z = handlers.Embedder(chanel.get_channel(), 'Title', 'Description', 0xffffff)
		 await z.send()
		 await y.send()
		 return

		 	

		







obj.client.run('MzUzNjE3MTc2NzkzNzEwNjEy.DIyULg.7J9_CWDYHr2PGeFJWmnPhRLV8BU')



# https://discordapp.com/oauth2/authorize?client_id=353617176793710612&scope=bot&permissions=0x00000008