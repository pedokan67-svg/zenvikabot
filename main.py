import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = os.getenv("BOT_TOKEN")

async def main():
    logging.basicConfig(level=logging.INFO)
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is not set")
    bot = Bot(TOKEN)
    dp = Dispatcher()

    @dp.message(CommandStart())
    async def on_start(msg: types.Message):
        await msg.answer("Привет! Я ZenVikaBot 🌿 Готова.")

    @dp.message()
    async def echo(msg: types.Message):
        await msg.answer(msg.text)

    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
