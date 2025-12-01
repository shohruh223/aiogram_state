from aiogram import types, Router, F
from aiogram.filters import Command
from keyboard.default_keyboard import main_keyboard, crud_keyboard

router = Router()


@router.message(Command('start'))
async def send_message(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}",
                         reply_markup=main_keyboard())


@router.message(F.text == "User")
async def send_message(message: types.Message):
    await message.answer(f"Ma'lumotlarni tanlang",
                         reply_markup=crud_keyboard())








