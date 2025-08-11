# app/handlers/basic.py
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import logging

router = Router()

# --- Клавиатуры ---
kb_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📅 Записаться")],
        [KeyboardButton(text="💰 Цены")],
        [KeyboardButton(text="📲 Связаться с мастером")],
    ],
    resize_keyboard=True
)

kb_cancel = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="❌ Отмена")]],
    resize_keyboard=True
)

# --- Анкета (FSM) ---
class Booking(StatesGroup):
    name = State()
    car = State()
    date = State()
    phone = State()

@router.message(CommandStart())
async def cmd_start(m: Message):
    logging.info(f"/start от {m.from_user.id}")
    await m.bot.send_message(
        m.chat.id,
        "Привет! Я онлайн на Railway ✅\n\nВыберите действие:",
        reply_markup=kb_main
    )

@router.message(F.text == "💰 Цены")
async def prices(m: Message):
    await m.answer(
        "Диагностика Mercedes:\n"
        "• Базовая проверка — от 50 BYN\n"
        "• Расширенная с тестами — от 90 BYN\n"
        "Точный расчёт после первичной заявки.",
        reply_markup=kb_main
    )

@router.message(F.text == "📲 Связаться с мастером")
async def contact(m: Message):
    await m.answer("Связаться с мастером: @u_468345698", reply_markup=kb_main)

# --- Запись: запуск анкеты ---
@router.message(F.text == "📅 Записаться")
async def start_booking(m: Message, state: FSMContext):
    await state.set_state(Booking.name)
    await m.answer("Как вас зовут?", reply_markup=kb_cancel)

@router.message(Booking.name, F.text)
async def booking_name(m: Message, state: FSMContext):
    await state.update_data(name=m.text.strip())
    await state.set_state(Booking.car)
    await m.answer("Модель и год автомобиля? (например: W204, 2013)")

@router.message(Booking.car, F.text)
async def booking_car(m: Message, state: FSMContext):
    await state.update_data(car=m.text.strip())
    await state.set_state(Booking.date)
    await m.answer("Удобная дата/время? (например: завтра после 16:00)")

@router.message(Booking.date, F.text)
async def booking_date(m: Message, state: FSMContext):
    await state.update_data(date=m.text.strip())
    await state.set_state(Booking.phone)
    await m.answer("Телефон для связи (можно с Telegram username).")

@router.message(Booking.phone, F.text)
async def booking_phone(m: Message, state: FSMContext):
    await state.update_data(phone=m.text.strip())
    data = await state.get_data()
    await state.clear()

    # Итог для клиента
    msg = (
        "✅ Заявка принята!\n\n"
        f"Имя: {data['name']}\n"
        f"Авто: {data['car']}\n"
        f"Когда: {data['date']}\n"
        f"Контакт: {data['phone']}\n\n"
        "Мастер свяжется с вами для подтверждения."
    )
    await m.answer(msg, reply_markup=kb_main)

    # Здесь же можно отправить заявку тебе в личку/группу:
    # await m.bot.send_message(<YOUR_CHAT_ID>, f"Новая заявка: ...")

# Отмена анкеты
@router.message(F.text.lower() == "❌ отмена")
@router.message(Command("cancel"))
async def cancel(m: Message, state: FSMContext):
    await state.clear()
    await m.answer("Отменил. Возвращаюсь в меню.", reply_markup=kb_main)

# Простое эхо на остальное (чтобы всегда был ответ)
@router.message(F.text)
async def echo(m: Message):
    await m.answer(f"Эхо: {m.text}", reply_markup=kb_main)
