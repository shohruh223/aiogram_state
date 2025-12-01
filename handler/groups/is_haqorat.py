import asyncio
from aiogram import types, Router, F
from filters.group_chat import IsGroup

router = Router()


list = ["ahmoq", "jinni", "odobsiz"]
@router.message(IsGroup(), F.text.func(lambda text: any(word in text.lower() for word in list)))
async def handle_insults(message: types.Message):
    data = await message.reply("Iltimos, odobli bo'ling!")
    await message.delete()
    await asyncio.sleep(2)
    await data.delete()
