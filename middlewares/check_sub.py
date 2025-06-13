#ПРОВЕРКА ПОДПИСКИ НА КАНАЛ

# class SubscriptionMiddleware:
#     async def on_pre_process_message(self, message: types.Message, data: dict):
#         if not await check_subscription(message.from_user.id):
#             await message.answer("Подпишитесь на канал!")
#             raise CancelHandler()