class Settings:
    # # # Console settings

    # Set this to True if you want things output to the console ; Will not display below commands if False
    console_log = False

    # Set this to True if you want outgoing messages logged to console
    send_log = False

    # Set this to True if you want incoming messages logged to console
    recieved_log = False


    # # # Discord API Settings

    # Discord Bot Token
    bot_token = ''

    # Webhook for discord channel
    webhook = ''

    # Your Discord ID
    personal_id = ''

    # ID of channel with webhook in discord
    channel_id = ''


    # # # TextNow API Settings
    
    # Phone number to message
    number = ''

    # Name of person you are messaging ; Can be any string
    name = ''

    # TextNow username
    username = ''

    # sid_cookie for TextNowApi
    sid = ''

    # csrf_cookie for TextNowApi
    csrf = ''
