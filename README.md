# TextNow_Discord_Mirror

## Dependencies

* [`requests`](https://github.com/psf/requests)
* [`PIL`](https://github.com/python-pillow/Pillow)
* [`pytextnow`](https://github.com/leogomezz4t/PyTextNow_API)
* [`discord.py`](https://github.com/Rapptz/discord.py)

## Setup

* Create an account for [TextNow](https://www.textnow.com/)
* Create a [discord bot](https://discord.com/developers/applications) and copy the API key
  * Invite the discord bot to your server and optionally create a channel only you can see and message in
* Create a [dicord webhook](https://discord.com/developers/docs/resources/webhook) for a specific channel in your server
  * Copy the webhook url
  <img width="400" height="400" scr="https://user-images.githubusercontent.com/99856216/189783284-3c545ff8-c4d5-4e0d-a564-f936ab4b89c4.png">
* Fill out the `settings.py` file
  * To find the `channel_id`, right click on the channel you want to use for messaging
<p align="center">
  <img width="200" height="400" src="https://user-images.githubusercontent.com/99856216/189784416-02e6fa44-29a8-4628-b0db-dfc00d1c0453.png">
</p>
