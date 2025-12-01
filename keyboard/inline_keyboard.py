from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from database import db, User
from loader import GROUP_ID


def all_user_inline():
    users = db.query(User).all()
    buttons = []
    for user in users:
        button = InlineKeyboardButton(text=f"{user.name}",
                                      callback_data=f"{user.id}")
        buttons.append(button)

    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            buttons
        ]
    )
    return ikm


