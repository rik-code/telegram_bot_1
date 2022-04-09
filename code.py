import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    stick = open('sticker_telegram/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, stick)

    # keybord
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🔍 Поиск рандомного числа...')
    item2 = types.KeyboardButton('☺ Какие дела?')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Приветик, {0.first_name}!\n - <b>{1.first_name}</b>, бот созданный для того чтобы говорить тебе привет и другое.'.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot1(message):
    if message.chat.type == 'private':
        if message.text == '🔍 Поиск рандомного числа...':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == '☺ Какие дела?':
            bot.send_message(message.chat.id, 'Отлично сам как?')
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😔')

# RUN
bot.polling(none_stop=True)