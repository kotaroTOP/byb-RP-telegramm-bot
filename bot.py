import telebot
from telebot import types
import random
import pathlib
from pathlib import Path
import tokenT
import boarclass
from boarclass import Boar
from boarclass import my_boar

bot = tokenT.bot

Namebd = open('db/Name.db','rb')

print(Namebd)

Levelbd = open('db/Level.db','rb')

print(Levelbd)

PacksCountingbd = open('db/PacksC.db','rb')

print(PacksCountingbd)

level = '0'
name = 'player'
packs = 'Покачто вы не сделали ни один пак РП комманд'

@bot.message_handler(commands=['bybrules'])
def byb(message):
    bot.send_message(message.chat.id, 'ЪУЪ не удалять не забирать не изменять не подделывать не переделывать не ухудшать не красть ЪУЪ')

@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Ъуъ', callback_data='variants_button')
    item2 = types.InlineKeyboardButton('Профиль', callback_data='profile')
    item3 = types.InlineKeyboardButton('РП комманды', callback_data='RPcommands')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id,'Выбери', reply_markup=markup)

@bot.message_handler(commands=['chthp'])
def chthp(message):
    bot.send_message(message.chat.id,'Чат тех поддержки: https://t.me/+d7ctotwuMBQ1MjMy')

@bot.message_handler(commands=['variants'])
def variants(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Кнопки', callback_data='button1')
    item2 = types.InlineKeyboardButton('Картинка', callback_data='button2')
    item3 = types.InlineKeyboardButton('Текст', callback_data='button3')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id,'Выбери', reply_markup=markup)

@bot.message_handler(commands=['profile'])
def profile(message):
    bot.send_message(message.chat.id,'Ваш профиль',name,':')
    bot.send_message(message.chat.id,'Имя:',name)
    bot.send_message(message.chat.id,'Созданные РП паки:',packs)   
    bot.send_message(message.chat.id,'Уровень:',level,)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'profile':
            bot.send_message(call.message.chat.id,'Ваш профиль',name,':')
            bot.send_message(call.message.chat.id,'Имя:',name)
            bot.send_message(call.message.chat.id,'Созданные РП паки:',packs)   
            bot.send_message(call.message.chat.id,'Уровень:',level,)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'variants_button':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton('Кнопки', callback_data='button1')
            item2 = types.InlineKeyboardButton('Картинка', callback_data='button2')
            item3 = types.InlineKeyboardButton('Текст', callback_data='button3')
            markup.add(item1, item2, item3)
            bot.send_message(call.message.chat.id,'Выбери', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'button3':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton('⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜', callback_data='button')
            item2 = types.InlineKeyboardButton('⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛', callback_data='button')
            item3 = types.InlineKeyboardButton('⬜⬛⬛⬜⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬜', callback_data='button')
            item4 = types.InlineKeyboardButton('⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜ ', callback_data='button')
            item5 = types.InlineKeyboardButton('⬜⬛⬛🟩⬛⬛⬛⬛⬛🟩⬛⬛⬛⬜⬜', callback_data='button')
            item6 = types.InlineKeyboardButton('⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜', callback_data='button')
            item7 = types.InlineKeyboardButton('⬜⬛⬛⬛🟫⬛🟫⬛🟫⬛⬛⬛⬛⬛⬜', callback_data='button')
            item8 = types.InlineKeyboardButton('⬜⬛⬛⬛⬛🟫⬛🟫⬛⬛⬛⬛⬛⬛⬜', callback_data='button')
            item9 = types.InlineKeyboardButton('⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜', callback_data='button')
            item10 = types.InlineKeyboardButton('⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜', callback_data='button')
            item11 = types.InlineKeyboardButton('⬜⬜⬛⬛⬛⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜', callback_data='button')
            item12 = types.InlineKeyboardButton('⬜⬜⬛⬛⬛⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜', callback_data='button')
            item13 = types.InlineKeyboardButton('⬜⬜⬛⬛⬛⬛⬜⬜⬜⬛⬛⬛⬛⬜⬜', callback_data='button')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13)
            bot.send_message(call.message.chat.id, '.')

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'button2':
                bot.send_message(call.message.chat.id, 'https://cdn.discordapp.com/attachments/1164637220456632381/1208365770325758044/17-02-2024_134404.png?ex=65e30551&is=65d09051&hm=bf537d980d0b5410e10307e03315781f122850074658f6a3d75194e0c70c0a2d&')

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'button3':
            bot.send_message(call.message.chat.id, '!ЪУЪ!')

@bot.message_handler(commands=['byb'])
def profile(message):
    bot.send_message(message.chat.id, '!ЪУЪ!')


@bot.message_handler(commands=['boarclass'])
def profile(message):
    bot.send_message(message.chat.id,'Имя кабана:', Boar.boar_name, 'Шерсть кабана:', Boar.fur_type, 'Цвет шерсти кабана:', Boar.fur)
    bot.send_message(message.chat.id,'Инфа про кабана:', my_boar.info)
bot.infinity_polling(print('Bot started'))
