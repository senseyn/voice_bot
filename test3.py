import asyncio
import logging
#=========СЕТЕВЫЕ БИБЛИОТЕКИ=========
from aiogram.exceptions import TelegramNetworkError
from aiohttp import ClientConnectorError
#=========БИБЛИОТЕКИ СТАНДАРТ========
from aiogram.enums import ChatAction
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, BotCommand, BotCommandScopeDefault
#==========ИМПОРТ МОИХ ФАЙЛОВ=========
from handlers.welcome import print_start_banner
from handlers.style_text import start_text_bot, stop_text_bot, bot_text_baner

#=====================================

logging.basicConfig(level=logging.INFO,
                    format="\033[1;30;47m%(asctime)s - %(name)s - %(levelname)s - %(message)s\033[0m",
                    datefmt='%Y-%m-%d %H:%M:%S')  # Формат: ГГГГ-ММ-ДД ЧЧ:ММ:СС
logger = logging.getLogger(__name__)

bot = Bot(token='7808838750:AAGkavfg9KKEfLbrPaC9Z0noGXQWmb8GqEU')
dp = Dispatcher(storage=MemoryStorage())
start_router = Router()


#======================СОЗДАНИЕ СПИСКА КОМАНД================
async def set_commands():
    commands = [BotCommand(command='start', description='перезапуск бота'),
                BotCommand(command='play', description='тестовая функ'),
                BotCommand(command='s', description='тестовая функ')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


#=======================ЭКСПЕРИМЕНТЫ==========================
@start_router.message(F.text == "/start")
async def animate_text(message: types.Message):
    await message.delete()
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(0.5)
    name = message.from_user.first_name
    text = bot_text_baner(name)  #ОТПРАВЛЯЕМ И ПРИНИМАЕМ ТЕКСТ С ПАРАМЕТРОМ NAME
    await message.answer(text, parse_mode="HTML")


#=============================================================
@start_router.callback_query(F.data == "btn1")
async def callback_btn1(callback: types.CallbackQuery):
    await callback.message.answer("Вы нажали кнопку 1")
    await callback.answer()


@start_router.callback_query(F.data == "btn2")
async def callback_btn2(callback: types.CallbackQuery):
    await callback.message.answer("Вы нажали кнопку 2")
    await callback.answer()


async def main():
    try:
        dp.include_router(start_router)
        await bot.delete_webhook(drop_pending_updates=True)
        await set_commands()  # УСТАНОВКА МЕНЮ КОМАНД
        start_text_bot()
        print_start_banner()
        await dp.start_polling(bot)  #СТАРТ БОТА
    except (TelegramNetworkError, ClientConnectorError) as e:
        print("\033[1;41m⚠️ Сетевая ошибка: не удалось подключиться к Telegram API\033[0m")
        logging.error(f"[1;41mОшибка подключения: {e}")
    except Exception as e:
        print("\033[1;41m❌ Произошла непредвиденная ошибка.\033[0m")
        logging.exception(f"Критическая ошибка в работе бота: {e}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        stop_text_bot()
