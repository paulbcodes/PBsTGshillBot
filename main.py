import asyncio
from telethon import client
from telethon import events
from telethon.client import TelegramClient
import logging
import os
import json
from datetime import datetime

#delay in seconds between messages. Change number to alter delay.
latest_msg_send_delay = 2 

latest_msg = None

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
level=logging.INFO)
path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
os.chdir(path=path)
os.chdir("./data_store")
print(os.getcwd())

#set input and out channels from files
with open('channel_info.json', 'r') as openfile:
    channel_info = json.load(openfile)

Input_chat,receving_chat = channel_info["input_channel"],channel_info["receiving_channel"]

with open('telethon_vars.json', 'r') as openfile:
    telethon_vars = json.load(openfile)

#set user and start telegram
api_id,api_hash,phone_num = telethon_vars['api_id'],telethon_vars['api_hash'],telethon_vars['phone_num']
client = TelegramClient(phone_num,api_id,api_hash) 
client.start()


async def message():
    current_time = (datetime.now()).strftime("[%Y-%m-%d, %H:%M:%S]")
    await client.send_message('me', f'Your Program Started Succesfully... at {current_time}')

    for inputchannel in Input_chat:
        async for message in client.iter_messages(int(inputchannel),limit=1):
            print(f"\nLAST MESSAGE for {Input_chat[0]} was..")
            print(message.id, message.text)
    
    #message loop
    while True:
        if latest_msg is not None:
            for current_chat in receving_chat:
                try:
                    await client.send_message(int(current_chat), latest_msg)
                except:
                    pass
                await asyncio.sleep(latest_msg_send_delay) 
        else:
            await asyncio.sleep(5) 

client.loop.create_task(message())

for inputchannel in Input_chat:
    @client.on(events.NewMessage(chats=int(inputchannel)))
    async def test(event):
        global latest_msg
        print("_____________________________________________")
        print("Forwarded a message")
        print("_____________________________________________")
        latest_msg = event.message
client.run_until_disconnected()
