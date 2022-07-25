import pytextnow ; import asyncio
from discord import Webhook, AsyncWebhookAdapter
import aiohttp ; from settings import Settings
number = '+1' + Settings.number
text_now_client = pytextnow.Client(Settings.username,sid_cookie=Settings.sid,csrf_cookie=Settings.csrf)
async def send_msg(message):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(Settings.webhook,
        adapter=AsyncWebhookAdapter(session))
        await webhook.send(message, username=Settings.name)
if Settings.console_log:
    print('recieve.py started')
while True:
    new_messages = text_now_client.get_unread_messages()
    for message in new_messages:
        if number == message.number:
            asyncio.run(send_msg(message.content))
            if Settings.recieved_log and Settings.console_log:
                print(f'Recieved "{message.content}" from {Settings.name}')
        message.mark_as_read()