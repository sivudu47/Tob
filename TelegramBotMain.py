from telebot import types

import telebot
import os
import time


# Creates the bot based on the bot token.
bot = telebot.TeleBot("5920841797:AAF8_N4C2RDTdltaxHWdr6Iunoh09tU8Kco")

text_messages = {
    'start':
        u'Greetings! {} \n'
        u'I will help you with the below activities.\n\n'
        u'Press 1. View my total Pending amount\n'
        u'Press 2. View my pending bills\n'
        u'Press 3 (Menu) . For viewing this menu again later\n',

    'help':
        u"Sorry i couldn't understand"
}
@bot.message_handler(commands=['start'])
def send_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id, text_messages['start'].format(message.from_user.first_name),reply_markup=markup)
# Shows the menu

@bot.message_handler(regexp='^3$')
def send_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id, text_messages['start'].format(message.from_user.first_name),reply_markup=markup)
# Shows the menu

@bot.message_handler(regexp='^1 ')
def show_all_pending_bills(message):
    """output_message = "Pending Amount : WIP"
    bot.send_message(message.chat.id, output_message, parse_mode="Markdown")"""
    number = message.text.split(' ')[1]
    print(number)
    if number == "7010942886":
        for i in range(0,10000):
            time.sleep(1)
            bot.send_message(message.chat.id, str(i), parse_mode="Markdown")

@bot.message_handler(regexp='^2$')
def show_all_pending_bills(message):
    output_message = "Pending Bills :\n\nWIP"
    bot.send_message(message.chat.id, output_message, parse_mode="Markdown")

@bot.message_handler(func=lambda m : not m.text.startswith("/"), content_types=["text"])
def match_everything(message):
    bot.send_message(message.chat.id, text_messages['help'], parse_mode="Markdown")


# Starts the bot.
print("Going to start polling")
bot.infinity_polling()
