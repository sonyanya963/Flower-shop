import telebot
from telebot import types
token = "8453123900:AAFVyY7XA1vi0yGKf1-ZmPmHFjbW7BviDSQ"
mybot = telebot.TeleBot(token)

mybot.set_my_commands([
    types.BotCommand("start", "Начать работу с ботом"),
    types.BotCommand("menu", "Каталог"),
    types.BotCommand("orders", "История и статус заказов"),
    types.BotCommand("help", "Помощь"),
])

@mybot.message_handler(['start'])
def start(message):
    st1 = '''Добро пожаловать, это бот для заказа цветов.
    Для просмотра истории и статуса заказов нажмите /orders,
    для просмотра каталога нажмите /menu'''

    mybot.send_message(chat_id = message.chat.id, text = st1)

@mybot.message_handler(['menu'])
def menu(message):
    mt1 = 'Для просмотра асортимента используйте кнопки'
    mbt1 = "<-"
    mbt2 = "->"
    keyboard = types.InlineKeyboardMarkup()
    bmbt1 = types.InlineKeyboardButton (text = mbt1)
    bmbt2 = types.InlineKeyboardButton (mbt2)
    keyboard.add(mbt1, mbt2)
    mybot.send_photo(chat_id= message.chat.id, caption= "Лилии" + mt1, photo = "https://artflora.ru/blog/blagorodnaya-liliya-bah-bach-opisanie-i-foto/")



mybot.infinity_polling()