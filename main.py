#!/usr/bin/python

import asyncio
import configparser
import json

from async_faceit_api.dataclasses import Player
from telebot.async_telebot import AsyncTeleBot, logger
from faceit import AsyncFaceit
from telebot.types import Message, BotCommand, BotCommandScope, BotCommandScopeChatMember, BotCommandScopeDefault
from db_worker import BazaDBAsync

config = configparser.ConfigParser()
config.read('settings.ini')

tg_key = config["settings"]["TELEGRAM_API_KEY"]
faceit_key = config["settings"]["FACEIT_API_KEY"]

bot = AsyncTeleBot(tg_key, "MARKDOWN")
faceit = AsyncFaceit.data(faceit_key)
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

@bot.message_handler(commands=['search_player'])
async def search_ply_cmd(message):
    args = message.text.split(' ')

    try:
        awaitable = faceit.players.get(args[1])
        future = asyncio.ensure_future(awaitable)

        await asyncio.gather(future)
        try:
            player: Player = future.result()
            player_info = dict(player)
            await bot.reply_to(message, f"searching player results:\n"
                                        f"\n*Player ID*: {player.id}"
                                        f"\n*Player Country*: {player.country.upper()}"
                                        f"\n*Other Info:* {player_info}")
        except Exception as e:
            logger.error(e)

            await bot.reply_to(message, f"error while searching player: {e}")

    except Exception as e:
        logger.error(e)
        await bot.reply_to(message, f"error while send search request for player: {e}")

def main():
    bot.set_my_commands([
        BotCommand("roles", "Get Bot Roles"),
        BotCommand("help", "Bot Help"),
        BotCommand("search_player", "<player_name> return player info")
    ], language_code="en")

    bot.set_my_commands([
        BotCommand("roles", "Роли"),
        BotCommand("help", "Помощь"),
        BotCommand("search_player", "<player_name> поиск инфы о игроке")
    ], language_code="ru")

    asyncio.run(bot.polling())

if __name__ == '__main__':
    main()








