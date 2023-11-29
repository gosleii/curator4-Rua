import telebot
bot = telebot.TeleBot('6982100245:AAFk48ooIdq_VENs7EiB2XCgPy649NoLlcE')

# Запускает бота
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добрый день.\nСписок всех моих команд:\n/who\n/YTlink\n/FunnyCommand\n/top', parse_mode='Markdown')

# Краткое описание бота
@bot.message_handler(commands=['who'])
def main(message):
    bot.send_message(message.chat.id, 'Я бот Seemann, созданым учеником "Марафон по Python 2.0"', parse_mode='Markdown')

# Отображает гипер-сыллку в сообщении
@bot.message_handler(commands=['YTlink'])
def main(message):
    bot.send_message(message.chat.id, 'Вот мой любимый [клип](https://youtu.be/srN1GsnBui8?si=Oqa-18VeMpYSNOdU)', parse_mode='Markdown')

# Смешная команда
@bot.message_handler(commands=['FunnyCommand'])
def main(message):
    bot.send_message(message.chat.id, '*print("Goodbye world", 0/0)*', parse_mode='Markdown')

# Список лучших языков програмирования.
@bot.message_handler(commands=['top'])
def main(message):
    bot.send_message(message.chat.id, 'Топ 5 языков програмирования\n1.Python\n2.Python\n3.Python\n4.Python\n5.Python', parse_mode='Markdown')

bot.infinity_polling()