#!/usr/bin/env python3
import requests
import sys

def telegram_bot_msgSender(msg):
    teleBot_token = "xxxxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    teleBot_chatID = "xxxxxxxxxxxx"
    send_msg = (
        "https://api.telegram.org/bot"
        + teleBot_token
        + "/sendMessage?chat_id="
        + teleBot_chatID
        + "&parse_mode=Markdown&text="
        + msg
    )
    response = requests.get(send_msg)
    return response.json()

telegram_bot_msgSender(sys.argv[1])
