## TextNow_Discord_Mirror

# Please note that this is only tested/working on Linux(Ubuntu) as of latest version

## Dependencies

* [`requests`](https://github.com/psf/requests)
* [`PIL`](https://github.com/python-pillow/Pillow)
* [`pytextnow`](https://github.com/leogomezz4t/PyTextNow_API)
* [`discord.py`](https://github.com/Rapptz/discord.py)

## Setup

* Create an account for [TextNow](https://www.textnow.com/)
* Create a [discord bot](https://discord.com/developers/applications) and copy the API key
  * Invite the discord bot to your server and optionally create a channel only you can see and message in
* Create a [discord Webhook](https://discord.com/developers/docs/resources/webhook) for a specific channel in your server
  * Copy the Webhook url ([Image](https://user-images.githubusercontent.com/99856216/189783284-3c545ff8-c4d5-4e0d-a564-f936ab4b89c4.png))
* Fill out the `settings.py` file
  * To find the `channel_id`, right click on the channel you want to use for messaging ([Image](https://user-images.githubusercontent.com/99856216/189784416-02e6fa44-29a8-4628-b0db-dfc00d1c0453.png))
    * Note : If you don't see options to copy ID when right clicking, enable developer options ([Image](https://user-images.githubusercontent.com/99856216/189804552-06a837f3-e147-494f-858f-b7c4f0347ebc.png))
  * To find `personal_id` copy your user id from discord ([Image](https://user-images.githubusercontent.com/99856216/189785842-e09faff8-f3ea-4866-85a9-5a554d4a8498.png))
  * For `number` and `name`, just enter the phone number and name of who you are messaging
    * Example : `number = '1234567890'` and `name = 'Steven'`
  * For the TextNowAPI settings, please consult [their github](https://github.com/leogomezz4t/PyTextNow_API#how-to-get-the-cookie)
* You should now be able to run `run.py` and be able to use SMS and MMS messaging with discord in that specific channel
