from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from app.states.booking import Booking
from app.keyboards.main import kb_main
from app.services.notifications import notify_all, make_card_buttons

router = Router()

@router.message(F.text == '📅 Записаться')
async def booking_start(msg: Message, state: FSMContext):
    await state.set_state(Booking.name)
    await msg.answer('Как вас зовут?')

@router.message(Booking.name)
async def booking_name(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await state.set_state(Booking.model)
    await msg.answer('Модель и год авто? (например: W204, 2011)')

@router.message(Booking.model)
async def booking_model(msg: Message, state: FSMContext):
    await state.update_data(model=msg.text)
    await state.set_state(Booking.issue)
    await msg.answer('Что беспокоит? (коротко)')

@router.message(Booking.issue)
async def booking_issue(msg: Message, state: FSMContext):
    await state.update_data(issue=msg.text)
    await state.set_state(Booking.date)
    await msg.answer('Когда удобно приехать? (дата/время)')

@router.message(Booking.date)
async def booking_date(msg: Message, state: FSMContext):
    await state.update_data(date=msg.text)
    await state.set_state(Booking.phone)
    await msg.answer('Оставьте номер телефона')

@router.message(Booking.phone)
async def booking_finish(msg: Message, state: FSMContext, bot: Bot):
    await state.update_data(phone=msg.text)
    data = await state.get_data()

    text = (
        '📩 <b>Новая заявка</b>\n'
        f'👤 Имя: {data.get("name")}\n'
        f'🚘 Модель: {data.get("model")}\n'
        f'🛠 Проблема: {data.get("issue")}\n'
        f'📅 Время: {data.get("date")}\n'
        f'📞 Телефон: {data.get("phone")}\n'
        f'🗣 От: @{msg.from_user.username or msg.from_user.id}'
    )

    markup = make_card_buttons()
    sent = await notify_all(bot, text, reply_markup=markup)

    if sent:
        await msg.answer('Спасибо! Заявка отправлена. Мы свяжемся с вами.', reply_markup=kb_main)
    else:
        await msg.answer('Спасибо! Заявка сохранена. Свяжемся в ближайшее время.', reply_markup=kb_main)

    await state.clear()
