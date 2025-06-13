#==========ПРОВЕРКА ПРАВ АДМИНА=========

# from aiogram.dispatcher.filters import BoundFilter
# from aiogram import types
#
# class IsAdmin(BoundFilter):
#     async def check(self, message: types.Message):
#         return message.from_user.id in ADMINS