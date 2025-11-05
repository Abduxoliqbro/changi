from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import Dispatcher, filters
from aiogram.dispatcher.filters import Command
from aiogram.utils import executor
import logging

API_TOKEN = "8078536942:AAEYmEsxor_i-d2zlTYVst52rL7qTNne4Lo"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Salom! Men aiogram 2.x bilan ishlaydigan botman 🤖")


@dp.message_handler(Command("help"))
async def help_command(message: types.Message):
    await message.answer("Bu bot yordamchi menyusidir.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
