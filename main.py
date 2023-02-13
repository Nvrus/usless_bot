import requests
from settings import TOKEN as bot_token
from settings import GROUP_CHAT_ID as chat_id


for i in range(5):
    requests.get('https://api.telegram.org/bot%s/sendMessage' % bot_token,
             params={
                 "chat_id": chat_id,
                 'text': 'My say hello very well'
             })
