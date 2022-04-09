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

            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton('Хорошо', callback_data='good')
            item2 = types.InlineKeyboardButton('Средне', callback_data='medium')
            item3 = types.InlineKeyboardButton('Плохо', callback_data='bad')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'Отлично сам как?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😔')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отлично 😀')
            elif call.data == 'medium':
                bot.send_message(call.message.chat.id, 'Держись 😉')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='☺ Какие дела?', reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Ты крутой и прошёл наш тест на настроение!!!')

    except Exception as e:
        print(repr(e))

# RUN
bot.polling(none_stop=True)