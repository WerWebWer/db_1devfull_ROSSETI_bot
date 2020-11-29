# -*- coding: utf8 -*- 

import telebot
from telebot import types
import time
import logging
import config
import json
from random import randint

bot = telebot.TeleBot(token = config.BOT_TOKEN)

data = [[-1] * 10 for i in range(100)]
count = 0

data_old = [[-1] * 10 for i in range(100)]
status = ["🟡 На расмотрении (этап 1/3)", "🟡 На расмотрении (этап 2/3)","🟡 На расмотрении (этап 3/3)", "🔴 Отклонена", "🟢 Одобрена"]
count_st = 2
# Клавиатура
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
keyboard1.row('Начать', 'Мои заявки', 'Помощь')

keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
keyboard2.row('Начать с начала', 'Помощь')

data_old[0][0] = "353383640"
data_old[0][1] = "Оптимизация производства"
data_old[0][2] = "Применение новых технологий для снижения затрат на производство продукта"
data_old[0][3] = "Категория 1"
data_old[0][4] = "Подкатегория 2"
data_old[0][5] = "от 100 000р до 500 000р"
data_old[0][6] = "от 1 месяца до 6 месяцев"
data_old[0][7] = "wow"
data_old[0][8] = "🟢 Одобрена"
data_old[0][9] = "Kirill Nepomiluev"

data_old[1][0] = "353383640"
data_old[1][1] = "Апгрейд тимбилдинга"
data_old[1][2] = "Улучшение условия труда, нетворкинга в рабочее и в не рабочее время"
data_old[1][3] = "Категория 1"
data_old[1][4] = "Подкатегория 2"
data_old[1][5] = "от 3 000 000р"
data_old[1][6] = "Затрудняюсь"
data_old[1][7] = "wow"
data_old[1][8] = "🔴 Отклонена"
data_old[1][9] = "Kirill Nepomiluev"


# Кнопка в сообщении
button1 = types.InlineKeyboardMarkup()
callback_button1 = types.InlineKeyboardButton(text="Оформить РИ", callback_data="start_ri")
callback_button2 = types.InlineKeyboardButton(text="Посмотреть заявки", callback_data="share")
button1.add(callback_button1)
button1.add(callback_button2)

button2 = types.InlineKeyboardMarkup()
callback_button1 = types.InlineKeyboardButton(text="Категория 1", callback_data="k1")
callback_button2 = types.InlineKeyboardButton(text="Категория 2", callback_data="k2")
button2.add(callback_button1)
button2.add(callback_button2)

button3 = types.InlineKeyboardMarkup()
callback_button1 = types.InlineKeyboardButton(text="Подкатегория 1", callback_data="kk1")
callback_button2 = types.InlineKeyboardButton(text="Подкатегория 2", callback_data="kk2")
button3.add(callback_button1)
button3.add(callback_button2)

button4 = types.InlineKeyboardMarkup()
callback_button1 = types.InlineKeyboardButton(text="Да", callback_data="yes")
callback_button2 = types.InlineKeyboardButton(text="Нет", callback_data="no")
button4.add(callback_button1)
button4.add(callback_button2)

button5 = types.InlineKeyboardMarkup()
callback_button1 = types.InlineKeyboardButton(text="до 100 000р", callback_data="money_0")
callback_button2 = types.InlineKeyboardButton(text="от 100 000р до 500 000р", callback_data="money_100")
callback_button3 = types.InlineKeyboardButton(text="от 500 000р до 3 000 000р", callback_data="money_500")
callback_button4 = types.InlineKeyboardButton(text="от 3 000 000р", callback_data="money_3000")
callback_button5 = types.InlineKeyboardButton(text="Затрудняюсь", callback_data="money_idk")
button5.add(callback_button1)
button5.add(callback_button2)
button5.add(callback_button3)
button5.add(callback_button4)
button5.add(callback_button5)

button6 = types.InlineKeyboardMarkup()
callback_button1 = types.InlineKeyboardButton(text="до 1 месяца", callback_data="time_0")
callback_button2 = types.InlineKeyboardButton(text="от 1 месяца до 6 месяцев", callback_data="time_1")
callback_button3 = types.InlineKeyboardButton(text="от 6 месяцев до 1 года", callback_data="time_6")
callback_button4 = types.InlineKeyboardButton(text="от 1 года", callback_data="time_12")
callback_button5 = types.InlineKeyboardButton(text="Затрудняюсь", callback_data="time_idk")
button6.add(callback_button1)
button6.add(callback_button2)
button6.add(callback_button3)
button6.add(callback_button4)
button6.add(callback_button5)




def find_id(id):
	for i in range (100):
		if data[i][0] == str(id):
			return i
	return -1
	print("error id == -1")
	
def clear_data_id(id):
	global data
	for i in range(8):
		data[id][i+1] = -1

def count_data_id(id):
	j = find_id(id)
	for i in range(10):
		if data[j][i] == -1:
			return i
	return 7

	


# Команды бота
@bot.message_handler(commands=['start'])
def start_message(message):

	if find_id(message.chat.id) == -1:
		global count
		global data
		data[count][0] = str(message.chat.id)
		count = count + 1
		name = str(message.from_user.first_name) + " " + str(message.from_user.last_name)
		data[count-1][9] = name
	else:
		clear_data_id(find_id(message.chat.id))

	bot.send_message(message.chat.id, 'Привет!', reply_markup = keyboard1)
	bot.send_message(message.chat.id, 'Оформим идею?\nНажми \"Начать\" внизу, чтобы начали формировать заявку')
	# dbworker.write_to_json(message.chat.id, 0)

@bot.message_handler(commands=['help'])
def help_message(message):
	bot.send_message(message.chat.id, 'Команда:\n/start - начать с начала\n/cancel - отмена всего', reply_markup = keyboard1)
	clear_data_id(find_id(message.chat.id))

@bot.message_handler(commands=['cancel'])
def cancel_message(message):
	bot.send_message(message.chat.id, 'Отмена действия, я могу помощь еще с чем-нибудь?', reply_markup = keyboard1)
	clear_data_id(find_id(message.chat.id))

@bot.message_handler(commands=['my'])
def my_message(message):
	clear_data_id(find_id(message.chat.id))
	bot.send_message(message.chat.id, 'Ваши заявки', reply_markup = keyboard1)
	k = 0
	for j in range(100):
		if data_old[j][0] == str(message.chat.id) or data_old[j][0] == str("471641060") or data_old[j][0] == str("353383640"):
			bot.send_message(message.chat.id, 'Ваша заявка №' + str(k+1)+ "\nСтатус: " + str(data_old[j][8]) + '\n\n📍 Название:\n'+ str(data_old[j][1]) + "\n📍 Описание:\n" + str(data_old[j][2]) + "\n📍 Категория:\n" + str(data_old[j][3]) + "\n📍 Подкатегория:\n" + str(data_old[j][4]) + "\n📍 Предполагаемый бюджет\n" + str(data_old[j][5]) + "\n📍 Предполагаемый срок\n" + str(data_old[j][6]))
			k = k + 1
	if k == 0:
		bot.send_message(message.chat.id, 'К сожалению, у вас нет заявок. \nМожете попробовать создать нажав ввнизу на кнопку \"Начать\"', reply_markup = keyboard1)
		

# Обработка сообщений
@bot.message_handler(content_types=['text'])
def send_text(message):
	global data
	msg_text = message.text.lower()


	i = count_data_id(message.chat.id)

	if msg_text == "помощь":
		help_message(message)
		return
	if msg_text == "мои заявки":
		my_message(message)
		return
	if msg_text == "начать с начала":
		start_message(message)
		return
	
	if i == 1:
		if msg_text == "начать":
			bot.send_message(message.chat.id, 'Этап 1/6\n\nНапишите название кратко и по сути предложения', reply_markup = keyboard2) #1
			return
		else:
			data[find_id(message.chat.id)][i] = msg_text
			bot.send_message(message.chat.id, 'Этап 2/6\n\nНапишите подробное описание', reply_markup = keyboard2) #2
	elif i == 2:
		data[find_id(message.chat.id)][i] = msg_text
		bot.send_message(message.chat.id, 'Отлично!', reply_markup = keyboard2)
		bot.send_message(message.chat.id, 'Этап 3/6\n\nВыберите категорию из предложенных ниже', reply_markup = button2) #2
	elif i == 7:
		j = find_id(message.chat.id)
		bot.send_message(message.chat.id, 'Ваша заявка\n\n📍 Название:\n'+ str(data[j][1]) + "\n📍 Описание:\n" + str(data[j][2]) + "\n📍 Категория:\n" + str(data[j][3]) + "\n📍 Подкатегория:\n" + str(data[j][4]) + "\n📍 Предполагаемый бюджет\n" + str(data[j][5]) + "\n📍 Предполагаемый срок\n" + str(data[j][6]))
		bot.send_message(message.chat.id, 'Отправляем?', reply_markup = button4)
	else:
		help_message(message)
		

	# print(data)



# В большинстве случаев целесообразно разбить этот хэндлер на несколько маленьких
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	global data_old
	global count_st
    # Если сообщение из чата с ботом
	i = count_data_id(call.message.chat.id)
	if call.message:
		if call.data == "k1":
			bot.send_message(chat_id=call.message.chat.id, text = 'Этап 4/6\n\nВыберите подкатегорите подкатегорию', reply_markup = button3)
			data[find_id(call.message.chat.id)][i] = "Категория 1"
		elif call.data == "k2":
			bot.send_message(chat_id=call.message.chat.id, text = 'Этап 4/6\n\nВыберите подкатегорите подкатегорию', reply_markup = button3)
			data[find_id(call.message.chat.id)][i] = "Категория 2"
		elif call.data == "kk1":
			bot.send_message(chat_id=call.message.chat.id, text = 'Этап 5/6\n\nВыберите требемый бюджет', reply_markup = button5)
			data[find_id(call.message.chat.id)][i] = "Подкатегория 1"
		elif call.data == "kk2":
			bot.send_message(chat_id=call.message.chat.id, text = 'Этап 5/6\n\nВыберите требемый бюджет', reply_markup = button5)
			data[find_id(call.message.chat.id)][i] = "Подкатегория 2"
		elif call.data == "money_0":
			bot.send_message(chat_id=call.message.chat.id, text = 'Этап 6/6\n\nВыберите необходимое время для внедрения', reply_markup = button6)
			data[find_id(call.message.chat.id)][i] = "до 100 000р"
		elif call.data == "money_100":
			bot.send_message(chat_id=call.message.chat.id, text = 'Этап 6/6\n\nВыберите необходимое время для внедрения', reply_markup = button6)
			data[find_id(call.message.chat.id)][i] = "от 100 000р до 500 000р"
		elif call.data == "money_500":
			bot.send_message(chat_id=call.message.chat.id, text = 'Этап 6/6\n\nВыберите необходимое время для внедрения', reply_markup = button6)
			data[find_id(call.message.chat.id)][i] = "от 500 000р до 3 000 000р"
		elif call.data == "money_3000":
			bot.send_message(chat_id=call.message.chat.id, text = 'Этап 6/6\n\nВыберите необходимое время для внедрения', reply_markup = button6)
			data[find_id(call.message.chat.id)][i] = "от 3 000 000р "
		elif call.data == "money_idk":
			bot.send_message(chat_id=call.message.chat.id, text = 'Этап 6/6\n\nВыберите необходимое время для внедрения', reply_markup = button6)
			data[find_id(call.message.chat.id)][i] = "Затрудняюсь"
		elif call.data == "time_0":
			data[find_id(call.message.chat.id)][i] = "до 1 месяца"
			send_text(call.message)
		elif call.data == "time_1":
			data[find_id(call.message.chat.id)][i] = "от 1 месяца до 6 месяцев"
			send_text(call.message)
		elif call.data == "time_6":
			data[find_id(call.message.chat.id)][i] = "от 6 месяцев до 1 года"
			send_text(call.message)
		elif call.data == "time_12":
			data[find_id(call.message.chat.id)][i] = "от 1 года"
			send_text(call.message)
		elif call.data == "time_idk":
			data[find_id(call.message.chat.id)][i] = "Затрудняюсь"
			send_text(call.message)
		elif call.data == "yes":
			bot.send_message(chat_id=call.message.chat.id, text = 'Отправляем руководству', reply_markup = keyboard1)
			j = find_id(call.message.chat.id)
			bot.send_message(chat_id=353383640, text = 'Новая заявка от ' + str(data[j][9]) + "\n\n📍 Название:\n"+ str(data[j][1]) + "\n📍 Описание:\n" + str(data[j][2]) + "\n📍 Категория:\n" + str(data[j][3]) + "\n📍 Подкатегория:\n" + str(data[j][4]) + "\n📍 Предполагаемый бюджет\n" + str(data[j][5]) + "\n📍 Предполагаемый срок\n" + str(data[j][6]), reply_markup = keyboard1)

			for i in range(10):
				data_old[count_st][i] = data[j][i]
			data_old[count_st][8] = status[1]
			count_st = count_st + 1
			clear_data_id(find_id(call.message.chat.id))
		elif call.data == "no":
			bot.send_message(chat_id=call.message.chat.id, text = 'Отменяем', reply_markup = keyboard1)
			clear_data_id(find_id(call.message.chat.id))
    # Если сообщение из инлайн-режима
	elif call.inline_message_id:
		if call.data == "test":
			bot.edit_message_text(inline_message_id=call.inline_message_id, text="Бдыщь")

if __name__ == "__main__":
	bot.infinity_polling()