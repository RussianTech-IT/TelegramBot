from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot_token = Bot('6053606091:AAFo5oXChwErb9Vratu4gqEto9OsJGMTcBs')
dp = Dispatcher(bot_token)

@dp.message_handler(commands=['start', 'hi'])
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}\nЧтобы увидеть список команд введите /help\nЧем я могу вам помочь?')
    
@dp.message_handler(commands=['help'])
async def getHelp(message: types.Message):
    await message.answer('Список моих поддерживаемых команд:\n\n/help - Список команд\n/site - Получить ссылку на сайт Russian Tech\n/github - Получить ссылку на наш GitHub')

@dp.message_handler(commands=['site', 'website', 'web'])
async def getSite(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://google.com'))
    await message.answer('Наш проект имеет свой собственный сайт, там можно найти кучу полезной информации, перейти можно на него по кнопке', reply_markup=markup)

@dp.message_handler(commands=['github'])
async def getGitHub(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('GitHub', url='https://google.com'))

    await message.answer('Наш проект имеет открытый исходный код, там можно изучить нашу работу, перейти можно на GitHub по кнопке', reply_markup=markup)

@dp.message_handler(commands=['get_materials']) # Output links materials (C++, Python, Java, C# and more...)
async def getResources(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть материалы', web_app=WebAppInfo(url='https://google.com')))

    await message.answer('Материалы для самостоятельного обучения различным языкам программирования и инструментов к ним можно найти, нажав на кнопку', reply_markup=markup)


executor.start_polling(dp)