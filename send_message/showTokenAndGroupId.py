import os
import telebot

bot = telebot.TeleBot(os.environ["TELEBOT_BOT_TOKEN"])

@bot.message_handler(commands=['token'])
def send_welcome(message):
	bot.reply_to(message, "TELEBOT_BOT_TOKEN:\n\t\t " + os.environ["TELEBOT_BOT_TOKEN"])

@bot.message_handler(commands=['group_id'])
def send_welcome(message):
	bot.reply_to(message, "GROUP_CHAT_ID: " + os.environ["GROUP_CHAT_ID"])

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
	
bot.infinity_polling()