import asyncio
from handler import setup_message_router
from loader import bot, dp, CHAT_ID
import logging

logging.basicConfig(level=logging.INFO)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    handler_router = setup_message_router()
    dp.include_router(handler_router)

    await bot.send_message(chat_id=CHAT_ID, text="Bot ishga tushdi")
    logging.warning("Bot ishga tushdi")
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())
