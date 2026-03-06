import telebot
import random
token = "8453123900:AAFVyY7XA1vi0yGKf1-ZmPmHFjbW7BviDSQ"
mybot = telebot.TeleBot(token)

@mybot.message_handler(['start'])
def start(message):
    st1 = 'Привет, отправь что-нибудь'

    mybot.send_message(chat_id = message.chat.id, text = st1)

@mybot.message_handler(func= lambda message: True)
def echo_all(message):
    if message.content_type != 'text':
        mybot.reply_to(message, 'Я работаю только с текстом.')
        return
    text = message.text
    if len(text) < 3:
        mybot.reply_to(message, 'Слишком короткий текст.')
    else:
        words = text.split()
        analysis = f"""Анализ сообщения:\nСимволов: {len(text)}\nСлов: {len(words)}\nПервое слово: {words[0]}"""
        mybot.reply_to(message, analysis)
mybot.infinity_polling()
