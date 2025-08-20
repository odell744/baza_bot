#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import asyncio

from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot('8367105335:AAHDrMBpgHCoQz7FRS6S_lD5xWhrgECaQcY')

tsx = 'asdaf'
data = {
    "msg_count": 0
}


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = f'Hi, I am EchoBot.\nJust write me something and I will repeat it! {data['msg_count']}'
    data['msg_count'] += 1
    await bot.reply_to(message, text)


@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)

asyncio.run(bot.polling())