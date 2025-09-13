#!/usr/bin/python

import asyncio
import configparser

from telebot.async_telebot import AsyncTeleBot, logger
from async_faceit_api import FaceitAPI
from telebot.types import Message, BotCommand, BotCommandScope, BotCommandScopeChatMember, BotCommandScopeDefault
from db_worker import BazaDBAsync

config = configparser.ConfigParser()
config.read('settings.ini')

tg_key = config["settings"]["TELEGRAM_API_KEY"]
faceit_key = config["settings"]["FACEIT_API_KEY"]

bot = AsyncTeleBot(tg_key, "MARKDOWN")
faceit = FaceitAPI(faceit_key)
db = BazaDBAsync()

@bot.message_handler(commands=['help'])
async def help_cmd(message: Message):
    cmds = await bot.get_my_commands(language_code=message.from_user.language_code, scope=BotCommandScope())

    text = "*Список команд бота*:\n" if message.from_user.language_code == "ru" else "Help:"

    for cmd in cmds:
        cmd_str = f"\n/{cmd.command} - {cmd.description}"
        text += cmd_str

    await bot.reply_to(message, text)

@bot.message_handler(commands=['roles'])
async def roles_cmd(message):
    roles = await db.get_roles()

    for role in roles:
        print(type(role))

    await bot.reply_to(message, roles)

def main():
    bot.set_my_commands([
        BotCommand("roles", "Get Bot Roles"),
        BotCommand("help", "Bot Help")
    ], language_code="en")

    bot.set_my_commands([
        BotCommand("roles", "Роли"),
        BotCommand("help", "Помощь")
    ], language_code="ru")

    asyncio.run(bot.polling())

if __name__ == '__main__':
    main()








