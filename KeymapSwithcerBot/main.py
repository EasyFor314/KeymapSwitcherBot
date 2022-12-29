import keymapSwitcher as switcher
import telebot
import config
import logging

bot = telebot.TeleBot(config.TOKEN)

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

@bot.message_handler(commands=["start", "help"])
def welcome(message):
    bot.send_message(message.chat.id, welcome_message.format(message.from_user))
    pass
                     
@bot.message_handler(commands=["entoru"])
def setEnglishMode(message):
    if switcher.getMode() == "english":
        bot.send_message(message.chat.id, "Режим 🇺🇸 ➡️ 🇷🇺 уже активен")
    else:
        switcher.setMode("english")
        bot.send_message(message.chat.id, "Режим 🇺🇸 ➡️ 🇷🇺 активирован")
        bot.send_message(message.chat.id, "Введите сообщение для перевода")
    pass
        
@bot.message_handler(commands=["rutoen"])                     
def setRussianMode(message):
    if switcher.getMode() == "russian":
        bot.send_message(message.chat.id, "Режим 🇷🇺 ➡️ 🇺🇸 уже активен")
    else:
        switcher.setMode("russian")
        bot.send_message(message.chat.id, "Режим 🇷🇺 ➡️ 🇺🇸 активирован")
        bot.send_message(message.chat.id, "Введите сообщение для перевода")
    pass


@bot.message_handler(content_types=["text"])
def switchKeymap(message: str):
    logging.basicConfig(level=logging.INFO, filename='myapp.log', format='%(asctime)s %(levelname)s:%(message)s')
    try:
        switcher.detect_mode(message.text)
        logging.info("Input id account = :" + str(message.from_user.id))
        if switcher.getMode() == "russian":
            result = switcher.russianToEnglish(message.text)
            bot.send_message(message.chat.id, result)
        elif switcher.getMode() == "english":
            result = switcher.englishToRussian(message.text)
            bot.send_message(message.chat.id, result)
        else:
            bot.send_message(message.chat.id, set_mode_message)
    except Exception as error:
        logging.error('Возникла ошибка {0}'.format(str(error)))
        bot.send_message(message.chat.id, "Произошла ошибка, повторите позднее")

bot.polling(none_stop=True)
