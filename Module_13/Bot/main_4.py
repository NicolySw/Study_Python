from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

api = "7905148297:AAFa22bbG_ZIQB7FsgpDv9-IImLADqZCr60"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Информация')
button_2 = KeyboardButton(text='Начало')
kb.add(button)
kb.add(button_2)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет', reply_markup=kb)


@dp.message_handler(text='Информация')
async def inform(message: types.Message):
    await message.answer('Информация о боте!')

# kb.row kb.insert()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)