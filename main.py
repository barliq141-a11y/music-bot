import telebot

TOKEN = "7994711953:AAEtobbSsVlT2rubTBKFZhRI-5gEJtQl3SQ"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salom jigar 👋 Music bot ishlayapti 🎵")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.send_message(message.chat.id, "Buyruqlar:\n/start - boshlash\n/help - yordam")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "Men hozir faqat oddiy botman 😄")

bot.polling()
