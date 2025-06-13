import logging
#=========БИБЛИОТЕКИ СТАНДАРТ========
from aiogram import Dispatcher, Bot, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage #БИБЛИОТЕКА ДЛЯ ХРАНЕНИЯ ДАННЫХ В ОПЕРАТИВНОЙ ПАМЯТИ
#from aiogram.fsm.storage.redis import RedisStorage #ЛУЧШИЙ ВАРИАНТ ДЛЯ ПРОДАКШЕНА
from decouple import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
#==========ИМПОРТ МОИХ ФАЙЛОВ=========
from db_handler.db import PostgresHandler
#=====================================
#redis = Redis.from_url(config("REDIS_URL"))  # Подключаем Redis / Redis(host='localhost', port=6379)
#storage_redis = RedisStorage(redis)

pg_db = PostgresHandler(config("PG_LINK"))
scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
admins = [int(admin_id) for admin_id in config("ADMINS").split(",")]

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt='%Y-%m-%d %H:%M:%S') # Формат: ГГГГ-ММ-ДД ЧЧ:ММ:СС
logger = logging.getLogger(__name__)

bot = Bot(token=config("TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage()) #ОБРАБОТЧИК СООБЩЕНИЙ СОХРАНЯЕТ ДАННЫЕ В ОПЕРАТИВНОЙ ПАМЯТИ
#dp = Dispatcher(storage=storage_redis)  #ОБРАБОТЧИК СООБЩЕНИЙ СОХРАНЯЕТ ДАННЫЕ В REDIS