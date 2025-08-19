from aiogram import types, Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

router = Router()

class Anketa(StatesGroup):
    name = State()
    age = State()

@router.message(lambda m: m.text == "Заполнить анкету")
async def start_anketa(message: types.Message, state: FSMContext):
    await message.answer("Как тебя зовут?")
    await state.set_state(Anketa.name)

@router.message(Anketa.name)
async def anketa_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Сколько тебе лет?")
    await state.set_state(Anketa.age)

@router.message(Anketa.age)
async def anketa_age(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(f"Анкета сохранена! Имя: {data['name']}, Возраст: {message.text}")
    await state.clear()
