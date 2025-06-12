import asyncio
import logging

from aiogram.enums import ChatAction
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt='%Y-%m-%d %H:%M:%S') # Формат: ГГГГ-ММ-ДД ЧЧ:ММ:СС
logger = logging.getLogger(__name__)

bot = Bot(token='7808838750:AAGkavfg9KKEfLbrPaC9Z0noGXQWmb8GqEU')
dp = Dispatcher(storage=MemoryStorage())
start_router = Router()


@start_router.message(F.text == "/start")
async def start_handler(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Кнопка 1", callback_data="btn1")],
        [InlineKeyboardButton(text="Кнопка 2", callback_data="btn2")]
    ])
    await message.answer("Выберите кнопку:", reply_markup=keyboard)


@start_router.message(F.text == "/play")
async def handle_play_message(message: Message):
    # Показываем действие "играет в игру"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(1)
    # Здесь может быть логика вашей игры
    await message.answer("Вы начали игру!")


@start_router.callback_query(F.data == "btn1")
async def callback_btn1(callback: types.CallbackQuery):
    await callback.message.answer("Вы нажали кнопку 1")
    await callback.answer()


@start_router.callback_query(F.data == "btn2")
async def callback_btn2(callback: types.CallbackQuery):
    await callback.message.answer("Вы нажали кнопку 2")
    await callback.answer()


async def main():
    dp.include_router(start_router)
    print("БОТ ЗАПУЩЕН")
    await bot.delete_webhook(drop_pending_updates=True)
    print("..")
    print("..")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("БОТ ОСТАНОВЛЕН")

