import telebot
import day

token = '1479000661:AAGVKWZfff6Bk-Hy_lWqxbYjbH6ZY_2UAmw'
bot = telebot.TeleBot(token)

keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('Понедельник', 'Вторник', 'Среда')
keyboard.row('Четверг', 'Пятница', 'Суббота')
keyboard.row('Расписание пар')


def send(id, text):
    bot.send_message(id, text, reply_markup=keyboard)


@bot.message_handler(commands=['start'])
def answer(message):
    send(message.chat.id, 'Привет')


@bot.message_handler(content_types=['text'])
def main(message):
    id = message.chat.id
    msg = message.text

    if msg.lower() == 'понедельник':
        send(id, day.monday)
    elif msg.lower() == 'вторник':
        send(id, day.tuesday)
    elif msg.lower() == 'среда':
        send(id, day.wednesday)
    elif msg.lower() == 'четверг':
        send(id, day.thursday)
    elif msg.lower() == 'пятница':
        send(id, day.friday)
    elif msg.lower() == 'суббота':
        send(id, day.saturday)
    elif msg.lower() == 'расписание пар':
        send(id, day.time)
    else:
        send(id, 'Я не понимаю')


bot.polling(none_stop=True)
