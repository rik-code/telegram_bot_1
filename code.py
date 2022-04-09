import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    stick = open('sticker_telegram/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, stick)
    bot.send_message(message.chat.id, 'Приветик..., {0.first_name}!\n - <b{1.first_name}<\b>, бот созданный для того чтобы говорить тебе привет и другое.'.format(message.from_user, bot.get_me()), parse_mode='html')


@bot.message_handler(content_types=['text'])
def bot1(message):
    bot.send_message(message.chat.id, message.text)

# RUN
bot.polling(none_stop=True)