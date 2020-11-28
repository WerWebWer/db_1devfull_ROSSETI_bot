# -*- coding: utf8 -*- 

import telebot
from telebot import types
import time
import logging
import dbworker
import config
import json

bot = telebot.TeleBot(token = config.BOT_TOKEN)

data = []
count = 0

# Клавиатура
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
keyboard1.row('Начать', 'Мои заявки', 'Помощь')

keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
keyboard2.row('Начать с начала', 'Помощь')


# Кнопка в сообщении
button1 = types.InlineKeyboardMarkup()
callback_button1 = types.InlineKeyboardButton(text="Оформить РИ", callback_data="start_ri")
callback_button2 = types.InlineKeyboardButton(text="Посмотреть заявки", callback_data="start")
button1.add(callback_button1)
button1.add(callback_button2)

# Команды бота
@bot.message_handler(commands=['start'])
def start_message(message):
	global count
	count = count + 1
	data[count - 1].append(str(message.chat.id))
	bot.send_message(message.chat.id, 'Привет!', reply_markup = keyboard1)
	bot.send_message(message.chat.id, 'Оформим РИ?', reply_markup = button1)
	# dbworker.write_to_json(message.chat.id, 0)

@bot.message_handler(commands=['help'])
def help_message(message):
	bot.send_message(message.chat.id, 'Команда:\n/start - начать с начала\n/cancel - отмена всего', reply_markup = keyboard1)
	global data
	data = []

@bot.message_handler(commands=['cancel'])
def cancel_message(message):
	bot.send_message(message.chat.id, 'Отмена действия, я могу помощь еще с чем-нибудь?', reply_markup = keyboard1)
	global data
	data = []


# Обработка сообщений
@bot.message_handler(content_types=['text'])
def send_text(message):
	msg_text = message.text.lower()
	id = -1
	for i in range (len(data)):
		if data[i][0] == str(message.chat.id):
			id = i
			pass
	

	if msg_text == "помощь":
		help_message(message)
		pass
	
	if len(data) == 0:
		if msg_text == "начать":
			bot.send_message(message.chat.id, 'Выберите категорию', reply_markup = keyboard1) #1
			pass
		else:
			bot.send_message(message.chat.id, 'Оформим РИ?', reply_markup = keyboard1)
	elif len(data) == 1:
		bot.send_message(message.chat.id, 'Отлично!', reply_markup = keyboard1)
		data.append(msg_text)
		bot.send_message(message.chat.id, 'под категория', reply_markup = keyboard1) #2
	elif len(data) == 2:
		bot.send_message(message.chat.id, 'Отлично!', reply_markup = keyboard1)
		data.append(msg_text)
		bot.send_message(message.chat.id, 'Что то у вас 3', reply_markup = keyboard1) #3
	elif len(data) == 3:
		bot.send_message(message.chat.id, 'Отлично!', reply_markup = keyboard1)
		data.append(msg_text)
		bot.send_message(message.chat.id, 'Что то у вас 4', reply_markup = keyboard1) #4
		
	elif len(data) == 4:
		bot.send_message(message.chat.id, 'Отлично!', reply_markup = keyboard1)
		data.append(msg_text)
		bot.send_message(message.chat.id, 'Что то у вас 5', reply_markup = keyboard1)
		
	elif len(data) == 5:
		bot.send_message(message.chat.id, 'Отлично!', reply_markup = keyboard1)
		data.append(msg_text)
		bot.send_message(message.chat.id, 'Что то у вас 6', reply_markup = keyboard1)
	else:
		if msg_text == "да":
			bot.send_message(message.chat.id, 'Отправляем', reply_markup = keyboard1)
		elif msg_text == "нет":
			bot.send_message(message.chat.id, 'Отменяем', reply_markup = keyboard1)

		else:
			bot.send_message(message.chat.id, 'Отправляем?', reply_markup = keyboard1)

	print(data)



# В большинстве случаев целесообразно разбить этот хэндлер на несколько маленьких
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "test":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь")
    # Если сообщение из инлайн-режима
    elif call.inline_message_id:
        if call.data == "test":
            bot.edit_message_text(inline_message_id=call.inline_message_id, text="Бдыщь")



if __name__ == "__main__":
	bot.infinity_polling()