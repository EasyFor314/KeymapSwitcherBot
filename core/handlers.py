import logging
import re

from aiogram import Dispatcher
from aiogram import types

from core.metric import REQUEST_TIME, START_COUNTER
from core import switcher

def main_handlers(dp: Dispatcher):
    dp.register_message_handler(welcome, lambda message: message.text in ["start", "help"] )

    dp.register_message_handler(setEnglishMode, lambda message: message.text == "entoru" )
    dp.register_message_handler(setRussianMode, lambda message: message.text == "rutoen" )

    dp.register_message_handler(switchKeymap)



welcome_message = """Привет,{0.first_name}! 🤙🏼🤙🏼🤙🏼
Забыл изменить раскладку при наборе сообщения?🤦🏻‍♂️ 
Бот поможет тебе привести сообщение в читаемый вид 👍🏼👍🏼👍🏼 

У бота есть два режима:

1) 🇺🇸 ➡️ 🇷🇺 - изменяет английскую раскладку на русскую

2) 🇷🇺 ➡️ 🇺🇸 - изменяет русскую раскладку на английскую

Режим работы определяется автоматически при в воде текста
"""

set_mode_message = """ Выберите один из режимов:
Чтобы активировать  🇺🇸 ➡️ 🇷🇺 
отправь боту команду 👉🏼 /entoru

Чтобы активировать  🇷🇺 ➡️ 🇺🇸
отправь боту команду 👉🏼 /rutoen
"""
reg_pattern = ', \[[0-9]{2}.[0-9]{2}.[0-9]{4} [0-9]{1,2}:[0-9]{2}\]'
href_pattern = '(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])'

async def welcome(msg: types.Message):
    await msg.answer(welcome_message.format(msg.from_user))
                     
async def setEnglishMode(msg: types.Message):
    if switcher.getMode() == "english":
        await msg.answer("Режим 🇺🇸 ➡️ 🇷🇺 уже активен")
    else:
        switcher.setMode("english")
        await msg.answer("Режим 🇺🇸 ➡️ 🇷🇺 активирован")
        await msg.answer("Введите сообщение для перевода")
    pass
                     
async def setRussianMode(msg: types.Message):
    if switcher.getMode() == "russian":
        await msg.answer("Режим 🇷🇺 ➡️ 🇺🇸 уже активен")
    else:
        switcher.setMode("russian")
        await msg.answer("Режим 🇷🇺 ➡️ 🇺🇸 активирован")
        await msg.answer("Введите сообщение для перевода")
    pass


@REQUEST_TIME.time()
async def switchKeymap(msg: types.Message):
    try:
        START_COUNTER.inc()
        spl_lst = msg.text.split('\n')
        logging.info("spl_lst : " + str(spl_lst))
        output_msg = ''
        for item in spl_lst:
            if item:
                if re.search(reg_pattern, item) or re.search(href_pattern, item):
                    logging.info('Оставляем как есть')
                    output_msg += item + '\n'
                else:
                    switcher.detect_mode(item)
                    logging.info("Input id account = :" + str(msg.from_user.id))
                    if switcher.getMode() == "russian":
                        result = switcher.russianToEnglish(item)
                        output_msg += result + '\n'
                    elif switcher.getMode() == "english":
                        result = switcher.englishToRussian(item)  
                        output_msg += result + '\n'
        await msg.answer(output_msg)
    except Exception as error:
        logging.error('Возникла ошибка {0}'.format(str(error)))
        await msg.answer("Произошла ошибка, повторите позднее")
