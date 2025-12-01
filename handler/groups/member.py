import asyncio
from aiogram import types, Router, F
from filters.group_chat import IsGroup

router = Router()


@router.message(IsGroup(), F.new_chat_members)
async def handle_insults(message: types.Message):
    user_id = message.new_chat_members[0].username
    fullname = message.new_chat_members[0].full_name
    await message.answer(text=f"""
<a href='https://t.me/{user_id}'>{fullname}</a>
Xush kelibsiz
    """,
                         parse_mode="HTML")


@router.message(IsGroup(), F.left_chat_member)
async def handle_insults(message: types.Message):
    user_id = message.left_chat_member.username
    fullname = message.left_chat_member.full_name

    if message.from_user.id == message.left_chat_member.id:
        await message.answer(text=f"""
        <a href='https://t.me/{user_id}'>{fullname}</a>
        Guruhdan chiqib ketdi
            """,
                             parse_mode="HTML")
    else:
        await message.answer(text=f"""
        <a href='https://t.me/{user_id}'>{fullname}</a>
        Guruhdan chopildi
            """,
                             parse_mode="HTML")
