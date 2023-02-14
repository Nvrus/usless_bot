import telebot
from settings import TOKEN as bot_token
from settings import GROUP_CHAT_ID as chat_id
import sys
import random


bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['getdays'])
def getdays(message):
    with open('database.txt') as db:
        bot.send_message(message.chat.id, str(int(db.read()) +1))

# @bot.message_handler(commands=['gift'])
# def getdays(message):
#     with open('for_you.jpg') as db:
#         bot.send_photo(message.chat.id, photo=open('for_you.jpg', 'rb'))


if __name__ == '__main__':
    bot.polling(none_stop=True)
