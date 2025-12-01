from aiogram import Router
from handler.users import start, create_user, read, delete_user

def setup_message_router():
    router = Router()
    router.include_router(start.router)
    router.include_router(create_user.router)
    router.include_router(read.router)
    router.include_router(delete_user.router)
    return router