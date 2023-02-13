import telebot
from settings import TOKEN as bot_token
from settings import GROUP_CHAT_ID as chat_id


bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['getdays'])
def getdays(message):
    with open('database.txt') as db:
        bot.send_message(message.chat.id, str(int(db.read()) +1))

if __name__ == '__main__':
    bot.polling(none_stop=True)
