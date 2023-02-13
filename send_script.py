# bot send a message
import telebot
import schedule
from settings import TOKEN as bot_token
from settings import GROUP_CHAT_ID as chat_id
import time

def job(bot):
    with open('database.txt') as db:
        number = db.read()
        bot.send_message(chat_id, 'Осталось дней: ' + number)
        number = int(number)
    with open('database.txt', 'w') as db:
        db.write(str(number - 1))

bot = telebot.TeleBot(bot_token)
schedule.every(10).seconds.do(job, bot)

while True:
    schedule.run_pending()
    time.sleep(1)
