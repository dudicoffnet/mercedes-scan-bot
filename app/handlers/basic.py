
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import os

router = Router()

CHANNEL_ID = -1002076509155
MASTER_USERNAME = "u_468345698"
CHANNEL_OPEN_URL = "https://t.me/+3kyBWqh-b1lkZDEy"

BANNER_FILE_ID = os.getenv("BANNER_FILE_ID")
BANNER_URL = os.getenv("BANNER_URL")
GREETING_TEXT = os.getenv("GREETING_TEXT", "Оригинальная диагностика Mercedes\nXENTRY / DAS — от 30 рублей\n\nВыберите действие кнопкой ниже:")

kb_main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="📅 Записаться")],
    [KeyboardButton(text="💰 Цены")],
    [KeyboardButton(text="📲 Связаться с мастером")],
], resize_keyboard=True)
kb_cancel = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="❌ Отмена")]], resize_keyboard=True)

def channel_buttons():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Связаться в Telegram", url=f"https://t.me/{MASTER_USERNAME}")],
        [InlineKeyboardButton(text="Открыть канал", url=CHANNEL_OPEN_URL)],
    ])

class Booking(StatesGroup):
    name = State()
    car = State()
    date = State()
    phone = State()

@router.message(CommandStart())
async def cmd_start(m: Message, state: FSMContext):
    await state.clear()
    sent = False
    if BANNER_FILE_ID:
        try:
            await m.bot.send_photo(m.chat.id, BANNER_FILE_ID, caption=GREETING_TEXT)
            sent = True
        except Exception:
            pass
    if (not sent) and BANNER_URL:
        try:
            await m.bot.send_photo(m.chat.id, BANNER_URL, caption=GREETING_TEXT)
            sent = True
        except Exception:
            pass
    if not sent:
        await m.answer(GREETING_TEXT)
    await m.answer("Меню:", reply_markup=kb_main)

@router.message(F.text == "💰 Цены")
async def prices(m: Message):
    await m.answer("Диагностика с XENTRY/DAS — от 30 BYN\nКомплекс и доп. тесты обсудим после первичной заявки.", reply_markup=kb_main)

@router.message(F.text == "📲 Связаться с мастером")
async def contact(m: Message):
    await m.answer(f"Связаться с мастером: @{MASTER_USERNAME}", reply_markup=kb_main)

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
    await m.answer("Заявка принята! Мастер свяжется с вами для подтверждения.", reply_markup=kb_main)
    post = (
        "Диагностика мерседес\n"
        "📣 Новая заявка\n"
        f"🧑 Имя: {data['name']}\n"
        f"🚗 Модель: {data['car']}\n"
        f"🕒 Время: {data['date']}\n"
        f"📞 Телефон: {data['phone']}\n"
        f"🔗 От: @{m.from_user.username if m.from_user.username else m.from_user.id}"
    )
    try:
        await m.bot.send_message(CHANNEL_ID, post, reply_markup=channel_buttons())
    except Exception:
        await m.answer("Не получилось отправить в канал — проверь, что бот добавлен администратором в канал.")

@router.message(F.text.lower() == "❌ отмена")
async def cancel(m: Message, state: FSMContext):
    await state.clear()
    await m.answer("Отменил. Возвращаюсь в меню.", reply_markup=kb_main)

@router.message(F.text)
async def echo(m: Message):
    await m.answer(f"Эхо: {m.text}", reply_markup=kb_main)
