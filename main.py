

import discord
import asyncio
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import constants as constants
import variables as variables
import database as database
import command_handlers as handlers
import objects as obj
import classes as classes



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
	if (message.content.startswith(constants.PREFIX)):
		 msj = classes.Message(message)
		 checker = handlers.BasicChecker(msj)
		 checked = await checker.check()
		 if (checked):
		 	return
		 custom_checker = handlers.CustomChecker(msj)
		 checked = await custom_checker.check()
		 if (checked):
		 	await custom_checker.do(checked)
		 	return
		 uk = classes.Sender(message.channel, 'Unknown command')
		 await uk.send()
		 return

		 	

		







obj.client.run('MzUzNjE3MTc2NzkzNzEwNjEy.DIyULg.7J9_CWDYHr2PGeFJWmnPhRLV8BU')



# https://discordapp.com/oauth2/authorize?client_id=353617176793710612&scope=bot&permissions=0x00000008