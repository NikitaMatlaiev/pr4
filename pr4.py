import telebot

# Замість 'YOUR_TOKEN' вставте свій токен
API_TOKEN = '7797884279:AAGsEP3iK6F_xKjbUVmEWNmrl5baeZx0aCM'

bot = telebot.TeleBot(API_TOKEN)

# Обробка текстових повідомлень
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

if __name__ == "__main__":
    print("Бот запущений!")
    bot.infinity_polling()
