import logging
from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, Update
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import uvicorn
from contextlib import asynccontextmanager

bot = Bot(token='7808838750:AAGkavfg9KKEfLbrPaC9Z0noGXQWmb8GqEU',
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()
start_router = Router()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await bot.set_webhook(url="ССЫЛКА С ВЕБХУКОМ",
                          allowed_updates=dp.resolve_used_update_types(),
                          drop_pending_updates=True)
    yield
    await bot.delete_webhook()


app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@dp.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer('Привет!')


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/webhook")
async def webhook(request: Request) -> None:
    update = Update.model_validate(await request.json(), context={"bot": bot})
    await dp.feed_update(bot, update)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )

    uvicorn.run(app, host="0.0.0.0", port=5000)
