from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.callback_data import CallbackData

import logging
import os
import json
import time




logging.basicConfig(level=logging.INFO, filename="bot.log",filemode="w")

botpath = os.getcwd()

with open("Token.json","r+") as fl:
    Tfile = fl.read()
    try:
        TOKEN = json.loads(Tfile)["TOKEN"]
    except:
        TOKEN = input("введите токен (https://t.me/BotFather): ")
        fl.write(json.dumps({"TOKEN":TOKEN}, sort_keys=True, indent=4))

bot = Bot(TOKEN)
dp = Dispatcher(bot)

start_msg = """Привет {},
Этот бот сделан в рамках нашего проекта.
Чтобы узнать возможности этого бота напиши в этот чат /help
Приятного использования!!!
"""

help_msg = """Хорошо что ты это поинтересовался!
/start                     старотовое сообщение
/help                      это сообщение
/github                    ссылка на наш github
/materials                 материалы для обучения
"""
songs = {}
### not Telegram async func ###

    ## Telegram ##
def mes_inf(message, log=False):
    user_id = message.from_user.id
    user_fn = message.from_user.full_name
    m_time = time.asctime()
    text = message.text
    logmsg = f"[{user_id}:{user_fn}]] : [{text}]                                          {m_time}"
    if log:
        logging.info(f"{logmsg}\n\n")
    return user_fn, user_id, text, m_time

async def bot_reply(message, answer, markup=None, image=None):
    user_fn,user_id,text,m_time = mes_inf(message, log=False)
    log = f" BOT: [{user_id}:{user_fn}]] : [{answer}]                                       {m_time}"
    log = filter(lambda ch: ch not in "\n", log)
    string = ""
    for i in log:
        string += i
    logging.info(f"{string}\n\n")

    if markup:
        if image:
            await bot.send_photo(message.chat.id,photo=open(image,"rb"), reply_markup=markup,caption=answer)
        else:
            await message.answer(answer,reply_markup=markup)
    else:
        await message.reply(answer)

def is_admin(id):
    with open("admins.json","r") as admins:
        py_obj = json.loads(admins.read())
        if str(id) in list(py_obj.keys()):
            return True
        else:
            return False


    ## USERS ##
def add_user(message):
    user_fn,user_id,text,m_time = mes_inf(message,log=False)
    with open("users.json","r") as users:
        users = json.loads(users.read())
        if str(user_id) not in list(users.keys()):
            users.update({str(user_id):{"full name":user_fn, "time": m_time}})
    with open("users.json","w") as users1:
        users1.write(json.dumps(users,indent=4))



@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def somebody_added(message: types.Message):
    for user in message.new_chat_members:
        await message.reply(f"Wellcome to the club, {user.full_name}")

@dp.message_handler(commands=["start"])
async def on_start(message: types.Message):
    user_fn, user_id, text, m_time = mes_inf(message,log=True)
    add_user(message)
    await bot_reply(message, start_msg.format(user_fn))

@dp.message_handler(commands=["help"])
async def on_start(message: types.Message):
    user_fn, user_id, text, m_time = mes_inf(message,log=True)
    add_user(message)
    await bot_reply(message, help_msg)

@dp.message_handler(commands=["github"])
async def github(message: types.Message):
    user_fn, user_id, text, m_time = mes_inf(message, log=True)
    answer = """Наш проект имеет открытый исходный код,
    там можно изучить нашу работу,
    перейти можно на GitHub по кнопке
    """
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('GitHub', url='https://github.com/RussianTech-IT'))
    await bot_reply(message, answer,markup=markup,image="../images/github.png")


@dp.message_handler(commands=["site","web"])
async def site(message: types.Message):
    user_fn, user_id, text, m_time = mes_inf(message, log=True)
    answer = """Наш проект имеет свой собственный сайт,
    там можно найти кучу полезной информации,
    перейти можно на него по кнопке
    """
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Site', url='https://google.com'))
    await bot_reply(message, answer,markup=markup)

@dp.message_handler(commands=["materials","get_materials"])
async def materials(message: types.Message):
    user_fn, user_id, text, m_time = mes_inf(message, log=True)
    answer="""Материалы для самостоятельного обучения
    различным языкам программирования
    и инструментов к ним можно найти,
    нажав на кнопку
    """
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Materials', web_app=types.WebAppInfo(url='https://russiantech-it.github.io')))
    await bot_reply(message, answer,markup=markup)




if __name__ == "__main__":
    executor.start_polling(dp)
