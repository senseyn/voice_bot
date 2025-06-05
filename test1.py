import asyncio
import os
import subprocess

import speech_recognition as sr
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command

#from aiogram.fsm.storage.memory import MemoryStorage
#from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

#===============ПОДКЛЮЧЕНИЕ ТОКЕНА================
TOKEN = "7808838750:AAGkavfg9KKEfLbrPaC9Z0noGXQWmb8GqEU"
bot = Bot(TOKEN)
dp = Dispatcher()
r = sr.Recognizer()

#=================================================
FFMPEG_PATH = r'D:\Program\ffmpeg\bin\ffmpeg.exe'

#===============СОЗДАНИЕ КЛАВИАТУРЫ===============


#================КОМАНДЫ БОТА=====================
@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Привет! Отправь голосовое сообщение, и я пришлю его в MP3 и текст расшифровку.")


@dp.message(Command('help'))
async def help_command(message: types.Message):
    await message.answer(
        "<b>Это бот <i>AudioTranscriber</i> для обработки аудио сообщений.</b>\nОтправь голосовое сообщение, "
        "и я пришлю его в MP3 и его текст расшифровку.\n<b>Команды:</b>\nПерезапуск бота: /start\n",
        parse_mode='HTML')


@dp.message(F.voice)
async def handle_voice(message: types.Message):
    user_id = message.from_user.id
    file_ogg = f"{user_id}_voice.ogg"
    file_mp3 = f"{user_id}_voice.mp3"
    file_wav = f"{user_id}_voice.wav"

    try:
        await bot.download(message.voice.file_id, destination=file_ogg)

        # Используем FFMPEG_PATH для конвертации
        subprocess.call([FFMPEG_PATH, "-i", file_ogg, file_wav])

        try:
            with sr.AudioFile(file_wav) as source:
                audio = r.record(source)
            text = r.recognize_google(audio, language="ru-RU")
        except sr.UnknownValueError:
            text = "Не удалось распознать речь("
        except sr.RequestError as e:
            text = f"Ошибка сервиса распознавания: {e}"

        subprocess.call([FFMPEG_PATH, "-i", file_ogg, file_mp3])

        await message.answer_document(types.FSInputFile(file_mp3))
        await message.answer(f"*Текст из голосового:*\n`{text}`", parse_mode="Markdown")

    finally:
        # Удаляем временные файлы в любом случае
        for f in [file_ogg, file_mp3, file_wav]:
            if os.path.exists(f):
                os.remove(f)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
