from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "8786511287:AAHPjb79WEZQ2VWwqin6V2bC-RkJ3Xdar2E"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("📦 Карго-бот работает!\nОтправь заявку")

@dp.message_handler()
async def order(message: types.Message):
    await message.answer("✅ Принято:\n" + message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
