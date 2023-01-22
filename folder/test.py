from telethon import TelegramClient, events, sync
from time import sleep
import folder.client
client = folder.client.client

@events.register(events.NewMessage(pattern=".test"))
async def test(event):
	await event.edit("Salom Darknet")
	sleep(2)
	await event.edit("Salom Darknet off1cial")