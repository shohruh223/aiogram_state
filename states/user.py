from aiogram.fsm.state import StatesGroup, State


class UserAddState(StatesGroup):
    photo = State()
    name = State()
    age = State()
    address = State()


class UserDeleteState(StatesGroup):
    id = State()
    confirm = State()