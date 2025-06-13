#=========БИБЛИОТЕКИ СТАНДАРТ========
import asyncio

from aiogram import Router  # F - магический фильтр
from aiogram.enums import ChatAction
from aiogram.filters import CommandStart
from aiogram.types import Message, BotCommand, BotCommandScopeDefault

# ==========ИМПОРТ МОИХ ФАЙЛОВ=========
from create_bot import bot
from handlers.style_text import bot_text_baner

#=====================================
start_router = Router()


#======================СОЗДАНИЕ СПИСКА КОМАНД====================
async def set_commands():
    commands = [BotCommand(command='start', description='перезапуск бота'),
                BotCommand(command='cat', description='картинка кота'),
                BotCommand(command='s', description='тест')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


#======================КОМАНДЫ БОТА==============================
@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.delete()
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(0.5)
    name = message.from_user.first_name
    text = bot_text_baner(name)  #ОТПРАВЛЯЕМ И ПРИНИМАЕМ ТЕКСТ С ПАРАМЕТРОМ NAME
    await message.answer(text, parse_mode="HTML")
