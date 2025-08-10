from aiogram.fsm.state import State, StatesGroup

class Booking(StatesGroup):
    name = State()
    model = State()
    issue = State()
    date = State()
    phone = State()
