from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from environs import env

env.read_env()
API_TOKEN = env.str('API_TOKEN')
CHAT_ID = env.str('CHAT_ID')
GROUP_ID = env.str('GROUP_ID')

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=storage)
ADMIN_ID = "7761068272"