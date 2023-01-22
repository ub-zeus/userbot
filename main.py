from telethon import TelegramClient, events, sync
#


import folder.client, folder.test
#
client = folder.client.client
#
with client as friday:
	friday.add_event_handler(folder.test.test) 


	

client.start()
client.run_until_disconnected()