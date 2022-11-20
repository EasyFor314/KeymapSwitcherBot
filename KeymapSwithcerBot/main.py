import keymapSwitcher as switcher
import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

welcome_message = """Привет,{0.first_name}! 🤙🏼🤙🏼🤙🏼
Забыл изменить раскладку при наборе сообщения?🤦🏻‍♂️ 
Бот поможет тебе привести сообщение в читаемый вид 👍🏼👍🏼👍🏼 

У бота есть два режима:

1) 🇺🇸 ➡️ 🇷🇺 - изменяет английскую раскладку на русскую

2) 🇷🇺 ➡️ 🇺🇸 - изменяет русскую раскладку на английскую

Для начала работы необходимо выбрать один из режимов 👇🏼

Чтобы активировать первый режим:
отправь боту команду 👉🏼 /entoru

Чтобы активировать второй режим:
отправь боту команду 👉🏼 /rutoen"""

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
def switchKeymap(message):
    if switcher.getMode() == "russian":
        result = "Результат:\n" + switcher.russianToEnglish(message.text)
        bot.send_message(message.chat.id, result)
    elif switcher.getMode() == "english":
        result = "Результат:\n\n" + switcher.englishToRussian(message.text)
        bot.send_message(message.chat.id, result)
    else:
        bot.send_message(message.chat.id, "Выберите один из режимов")
        
bot.polling(none_stop=True)
