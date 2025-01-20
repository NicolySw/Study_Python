from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, StatesGroup, State
from aiogram.dispatcher.filters.builtin import Text

import asyncio

api = "7905148297:AAFa22bbG_ZIQB7FsgpDv9-IImLADqZCr60"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text="Calories")
async def set_age(message: types.Message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state):
    await state.update_data(age=float(message.text))
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state):
    await state.update_data(growth=float(message.text))
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state):
    await state.update_data(weight=float(message.text))
    data = await state.get_data()
    REE = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] + 5
    await message.answer(f'Ваша суточная норма {round(REE, 2)} килокалорий')
    await state.finish()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий вашему здоровью.'
                         ' Введите слово Calories')


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)