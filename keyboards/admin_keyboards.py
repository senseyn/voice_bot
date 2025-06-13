#====================КЛАВИАТУРА АДМИНОВ==========================
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("Настройки"), KeyboardButton("Корзина"))
    return kb
