import telebot
from telebot import types

bot = telebot.TeleBot('6053606091:AAFo5oXChwErb9Vratu4gqEto9OsJGMTcBs')

@bot.message_handler(commands=['start', 'website', 'web'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')

@bot.message_handler(commands=['help'])
def getHelp(message):
    bot.send_message(message.chat.id, '<b>Help</b> info!', parse_mode='html')

@bot.message_handler(commands=['site'])
def getSite(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://github.com/RussianTech-IT'))
    bot.send_message(message.chat.id, '<b>У нас так же имеется свой сайт, на него можно перейти по кнопке ниже:</b>\n\n', parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['github'])
def getSite(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на GitHub', url='https://github.com/RussianTech-IT'))
    bot.send_message(message.chat.id, '<b>У нас так же имеется открытый исходный код проекта, на него можно перейти по кнопке ниже:</b>\n\n', parse_mode='html', reply_markup=markup)

@bot.message_handler()
def info(message):
    if message.text.lower() == 'что надо':
        bot.send_message(message.chat.id, 'ниче')


bot.polling(non_stop=True)