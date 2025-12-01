from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_keyboard():
    button = KeyboardButton(text="User")
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button]
        ],
        resize_keyboard=True
    )
    return rkm


def crud_keyboard():
    button = KeyboardButton(text="Ma'lumotlarni ko'rish")
    button2 = KeyboardButton(text="Ma'lumotlarni qo'shish")
    button3 = KeyboardButton(text="Ma'lumotlarni tahrirlash")
    button4 = KeyboardButton(text="Ma'lumotlarni O'chirish")
    button5 = KeyboardButton(text="◀️ back")
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
            [button5],
        ],
        resize_keyboard=True
    )
    return rkm


def confirm_keyboard():
    button = KeyboardButton(text="Ha ✅")
    button2 = KeyboardButton(text="Yo'q ❌")
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2]
        ],
        resize_keyboard=True
    )
    return rkm


def back_keyboard():
    button = KeyboardButton(text="🔙 back")
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button]
        ],
        resize_keyboard=True
    )
    return rkm
