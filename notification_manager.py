import os
import requests
from dotenv import load_dotenv
load_dotenv()


class NotificationManager:

    def __init__(self):
        pass

    def send_sms(self, message):
        token = os.getenv("telegram_api_key")
        chat_id = os.getenv("my_telegram_chat_id")
        url_req = "https://api.telegram.org/bot" + token + \
            "/sendMessage" + "?chat_id=" + chat_id + "&text=" + message
        results = requests.get(url_req)
        print(results.status_code)
