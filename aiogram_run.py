import asyncio
import logging

#=========СЕТЕВЫЕ БИБЛИОТЕКИ=========
from aiogram.exceptions import TelegramNetworkError
from aiohttp import ClientConnectorError
#=========БИБЛИОТЕКИ СТАНДАРТ========
from create_bot import bot, dp
#==========ИМПОРТ МОИХ ФАЙЛОВ=========
from handlers.start import start_router, set_commands
from handlers.welcome import print_start_banner
from handlers.style_text import start_text_bot, stop_text_bot
#=====================================
# from work_time.time_func import send_time_msg

# def register_handlers(): #РЕГИСТРАЦИЯ ПРОВЕРКИ НА ПОДПИСКУ
# dp.register_message_handler(cmd_start, commands=['start'])

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

