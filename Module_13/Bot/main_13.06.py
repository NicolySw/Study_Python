from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import asyncio



def api_(file_name="key.txt"):
    file = open(file_name, "r")
    data = file.read()
    file.close()
    return data


api = api_()
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


kb = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text='Рассчитать'),
    KeyboardButton(text='Информация'))

inline_kbd = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text='Рассчитать норму калорий',
                         callback_data='calories'),
    InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas'))


@dp.message_handler(text="Рассчитать")
async def send_inline_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inline_kbd)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(
        '10·вес(кг) + 6.25·рост(см) – 5·возраст(лет) + 5')
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст (лет):')
    await call.answer()
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
                         ' Нажмите "Рассчитать"', reply_markup=kb)

@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Бот подсчитывает норму калорий по формуле Миффлина - Сан Жеора')

@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
