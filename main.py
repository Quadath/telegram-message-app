from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import EditMessageRequest

import time

# Remember to use your own values from my.telegram.org!
api_id = '19110082'
api_hash = 'a7dd11527616ba229c1dee2405588006'
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage())
async def my_event_handler(event):
    print(event.raw_text)
    # message = await client.send_message('Qunthunnan0', '0')
    
    # await client.edit_message(message, '10')
    # await client.edit_message(message, '100')
    # await client.edit_message(message, '1000')
    # await client.edit_message(message, '10000')
    # await client.edit_message(message, '100000')
    # await client.edit_message(message, '1000000')
    # await client.edit_message(message, '10000000')
    # await client.edit_message(message, '100000000')
    # for i in range(1000):
    #     await client.edit_message(message, str(i + 1))
    #     time.sleep(1 / 4)

client.start()
client.run_until_disconnected()