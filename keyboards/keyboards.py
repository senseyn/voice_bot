#====================КЛАВИАТУРА ПОЛЬЗОВОТЕЛЕЙ========================
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_admin_menu():
    kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
    kb_admin.add(KeyboardButton("Каталог"), KeyboardButton("Корзина"))
    return kb_admin