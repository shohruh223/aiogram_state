from aiogram import Bot

from loader import GROUP_ID


async def check_subscription(bot: Bot, user_id: int):
    member = await bot.get_chat_member(chat_id=f"@{GROUP_ID}", user_id=user_id)
    return member.status in ["member", 'administrator', 'creator']
