import logging
import telebot
from telebot import types




token = None
with open('token.txt') as f:
    token = f.read().strip()

bot = telebot.TeleBot(token)

value = ''
old_value = ''

logging.basicConfig(
    filename = "log.txt",
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)
if __name__ == '__main__':


    keyboard = telebot.types.InlineKeyboardMarkup()

    keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data='no'),
                 telebot.types.InlineKeyboardButton('C', callback_data='C'),
                 telebot.types.InlineKeyboardButton('<=', callback_data='<='),
                 telebot.types.InlineKeyboardButton('/', callback_data='/'))

    keyboard.row(telebot.types.InlineKeyboardButton('7', callback_data='7'),
                 telebot.types.InlineKeyboardButton('8', callback_data='8'),
                 telebot.types.InlineKeyboardButton('9', callback_data='9'),
                 telebot.types.InlineKeyboardButton('*', callback_data='*'))

    keyboard.row(telebot.types.InlineKeyboardButton('4', callback_data='4'),
                 telebot.types.InlineKeyboardButton('5', callback_data='5'),
                 telebot.types.InlineKeyboardButton('6', callback_data='6'),
                 telebot.types.InlineKeyboardButton('-', callback_data='-'))

    keyboard.row(telebot.types.InlineKeyboardButton('1', callback_data='1'),
                 telebot.types.InlineKeyboardButton('2', callback_data='2'),
                 telebot.types.InlineKeyboardButton('3', callback_data='3'),
                 telebot.types.InlineKeyboardButton('+', callback_data='+'))

    keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data='no'),
                 telebot.types.InlineKeyboardButton('0', callback_data='0'),
                 telebot.types.InlineKeyboardButton(',', callback_data='.'),
                 telebot.types.InlineKeyboardButton('=', callback_data='='))


    @bot.message_handler(commands=['start'])
    def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👋 Поздороваться")
        btn2 = types.KeyboardButton("❓ Калькулятор")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id, text="Привет, я БОТ!", reply_markup=markup)


    @bot.message_handler(content_types=['text'])
    def func(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👋 Поздороваться")
        btn2 = types.KeyboardButton("❓ Калькулятор")
        markup.add(btn1, btn2)
        if message.text == "👋 Поздороваться":
            logger.info(f'{message.from_user.first_name}, нажал кнопку Поздороваться')
            bot.send_message(message.chat.id, text="Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)
        elif message.text == "❓ Калькулятор":
            getMessage(message)
            bot.send_message(message.chat.id, text="Используй команду: /calculator", reply_markup=markup)
    #
    #
    @bot.message_handler(commands=['calculator'])
    def getMessage(message):
        global value
        if value == '':
            bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
        else:
            bot.send_message(message.from_user.id, value, reply_markup=keyboard)


    @bot.callback_query_handler(func=lambda call: True)
    def callback_func(query):
        global value, old_value
        data = query.data

        if data == 'no':
            pass
        elif data == 'C':
            value = ''
        elif data == '<=':
            if value != '':
                value = value[:len(value)-1]
        elif data == '=':
            try:
                value = str(eval(value))
            except:
                value = 'ошибка!'
        else:
            value += data

        if (value != old_value and value != '') or ('0' != old_value and value == ''):
            if value == '':
                bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0',
                                      reply_markup=keyboard)
                old_value = '0'
            else:
                bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value,
                                      reply_markup=keyboard)
                old_value = value
        if value == 'ошибка!': value = ''

    bot.polling(none_stop=False, interval=0)

