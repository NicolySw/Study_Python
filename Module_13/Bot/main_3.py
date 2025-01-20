from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, StatesGroup, State
from aiogram.dispatcher import FSMContext
import asyncio


def api_(file_name="key.txt"):
    file = open(file_name, "r")
    data = file.read()
    file.close()
    return data


api = api_()
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserStatesGroup(StatesGroup):
    adress = State()


@dp.message_handler(text=["Заказать"])
async def buy(message: types.Message):
    await message.answer("Отправь нам свой адрес!")
    await UserStatesGroup.adress.set()


@dp.message_handler(state=UserStatesGroup.adress)
async def fsm_handler(message: types.Message, state):
    await state.update_data(first=message.text)
    data = await state.get_data()
    await message.answer(f'Доставка будет отправлена на {data["first"]}')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)