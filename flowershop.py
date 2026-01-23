import telebot
from telebot import types
token = "8453123900:AAFVyY7XA1vi0yGKf1-ZmPmHFjbW7BviDSQ"
mybot = telebot.TeleBot(token)

@mybot.message_handler(['menu'])
def menu(message):
    mt1 = '''Добро пожаловать, это бот для заказа цветов. 
    Чтобы просмотреть каталог цветов и выбрать понравившиеся, 
    нажмите на кнопку под сообщением.'''

    mybot.send_message(chat_id = message.chat.id, text = mt1)
    



mybot.infinity_polling()