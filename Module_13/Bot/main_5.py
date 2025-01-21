from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
import asyncio
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def api_(file_name="key.txt"):
    file = open(file_name, "r")
    data = file.read()
    file.close()
    return data


api = api_()
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text="Информация", callback_data="info")
kb.add(button)

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="info")],
        [
            KeyboardButton(text="shop"),
            KeyboardButton(text="donate")
        ]
    ], resize_keyboard=True
)

# @dp.message_handler(commands=["start"])
# async def starter(message):
#     await message.answer("Рады вас видеть", reply_markup=kb)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Рады вас видеть", reply_markup=start_menu)


# @dp.callback_query_handler(text="info")
# async def infor(call):
#     await call.message.answer("Информация о боте")
#     await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
