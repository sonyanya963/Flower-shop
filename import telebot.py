import telebot
import random
token = "8453123900:AAFVyY7XA1vi0yGKf1-ZmPmHFjbW7BviDSQ"
mybot = telebot.TeleBot(token)

options = ['камень', 'ножницы', 'бумага']

@mybot.message_handler(['start'])
def start(message):
    st1 = '''Привет, давай играть в камень-ножницы-бумага! 
    Напиши один из вариантов в чат '''

    mybot.send_message(chat_id = message.chat.id, text = st1)

@mybot.message_handler(func= lambda message: True)
def game(message):
    user_choice = message.text.lower()
    bot_choice = random.choice(options)
    if user_choice not in options:
        mybot.send_message(message.chat.id, 'Выбери: камень, ножницы или бумага')
        return
    if user_choice == bot_choice:
        result = "Ничья"
    elif (user_choice == 'камень' and bot_choice == 'ножницы') or (user_choice == 'бумага' and bot_choice == 'камень') or (user_choice == 'ножницы' and bot_choice == 'бумага'):
        result = 'Ты выйграл!'
    else:
        result = 'Бот выйграл!'
    mybot.send_message(message.chat.id, f"Ты выбрал: {user_choice}\nЯ выбрал: {bot_choice}\n{result}")
mybot.polling()
