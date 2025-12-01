from aiogram import types, Router, F
from aiogram.filters import Command

from database import db, User
from keyboard.default_keyboard import main_keyboard, crud_keyboard
from keyboard.inline_keyboard import all_user_inline

router = Router()



@router.message(F.text == "Ma'lumotlarni ko'rish")
async def send_message(message: types.Message):
    users = db.query(User).all()
    for user in users:
        await message.answer_photo(photo=user.photo,
                                   caption=f"""{user.name}ning yoshi {user.age} da
Yashash manzili {user.address}""")


# @router.message(F.text == "Ma'lumotlarni ko'rish")
# async def send_message(message: types.Message):
#     await message.answer(text="Hamma userlar",
#                          reply_markup=all_user_inline())








