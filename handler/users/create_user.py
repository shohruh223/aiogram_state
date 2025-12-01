from aiogram import types, Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from database import User, db
from states.user import UserAddState

router = Router()


@router.message(F.text == "Ma'lumotlarni qo'shish")
async def send_message(message: types.Message, state: FSMContext):
    await message.answer(text="Rasmingizni kiriting")
    await state.set_state(UserAddState.photo)


@router.message(StateFilter(UserAddState.photo), F.photo)
async def send_message(message: types.Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    await state.update_data(photo=photo_id)
    await message.answer(text="Ismingizni kiriting")
    await state.set_state(UserAddState.name)


@router.message(StateFilter(UserAddState.name))
async def send_message(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text="Yoshingizni kiriting")
    await state.set_state(UserAddState.age)


@router.message(StateFilter(UserAddState.age))
async def send_message(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer(text="Manzil kiriting")
    await state.set_state(UserAddState.address)


@router.message(StateFilter(UserAddState.address))
async def send_message(message: types.Message, state: FSMContext):
    data = await state.get_data()
    photo = data.get("photo")
    name = data.get("name")
    age = data.get("age")
    address = message.text

    user = User(photo=photo,
                name=name,
                age=age,
                address=address)
    db.add(user)
    db.commit()
    db.close()

    await message.answer_photo(photo=photo,
                               caption=f"""{name}ning yoshi {age} da
Yashash manzili {address}""")
    await state.clear()
