from telebot import types
import telebot
import day

# ТОКЕН БОТА, МОЖНО ПОЛУЧИТЬУ @FATHER_BOT
bot = telebot.TeleBot("1479000661:AAHBFbKibQvqj6tErAcF2eNBl9lUIuO_zwo", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Доброго времени суток, что именно вам нужно?")


@bot.message_handler(commands=['время', 'пары'])
def send_schedule(message):
    bot.reply_to(message, day.time)


@bot.message_handler(commands=['понедельник'])
def send_schedule(message):
    bot.reply_to(message, day.monday + '\n Пожалуй один из самых тяжелых дней! <3')


@bot.message_handler(commands=['вторник'])
def send_schedule(message):
    bot.reply_to(message, day.tuesday)


@bot.message_handler(commands=['среда'])
def send_schedule(message):
    bot.reply_to(message, day.wednesday)


@bot.message_handler(commands=['четверг'])
def send_schedule(message):
    bot.reply_to(message, day.thursday)


@bot.message_handler(commands=['пятница'])
def send_schedule(message):
    bot.reply_to(message, day.friday)


@bot.message_handler(commands=['суббота'])
def send_schedule(message):
    bot.reply_to(message, day.friday)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
