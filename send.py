import discord ; import pytextnow ; import requests ; from PIL import Image
from io import BytesIO ; import os ; from settings import Settings

client = discord.Client()
text_now_client = pytextnow.Client(Settings.username,sid_cookie=Settings.sid,csrf_cookie=Settings.csrf)

@client.event
async def on_ready(): 
    if Settings.console_log: print('send.py started')

@client.event
async def on_message(message):
    # Checks to see if the message is from given ID and in specified channel
    if str(message.author.id) == Settings.personal_id and str(message.channel.id) == Settings.channel_id:
        try:
            # Checks if there is an attachment with a url
            url = message.attachments[0].url
        except IndexError:
            text_now_client.send_sms(Settings.number, message.content) # Sends the message
            if Settings.send_log and Settings.console_log: # Prints the message sent from discord to the console
                print(f'"{message.content}" sent to {Settings.name}')
        else:
            if url[0:26] == "https://cdn.discordapp.com": # Check if url is from discord
                try:
                    Image.open(BytesIO(requests.get(url).content)).save('cache.png') # Saves image
                    text_now_client.send_mms(Settings.number, 'cache.png') # Sends image
                    if Settings.send_log:
                        print(f'Image has been sent to {Settings.name}')
                    try:
                        os.remove('./cache.png') # Removes saved image
                    except Exception:
                        pass
                except Exception:
                    pass
client.run(Settings.bot_token)