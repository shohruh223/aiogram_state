from aiogram import types, Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from database import User, db
from keyboard.default_keyboard import confirm_keyboard, back_keyboard
from states.user import UserDeleteState

router = Router()


@router.message(F.text == "Ma'lumotlarni O'chirish")
async def send_message(message: types.Message, state: FSMContext):
    await message.answer(text="ID kiriting")
    await state.set_state(UserDeleteState.id)


@router.message(StateFilter(UserDeleteState.id))
async def send_message(message: types.Message, state: FSMContext):
    await state.update_data(id=message.text)
    await message.answer(text="O'chirishni tasdiqlang",
                         reply_markup=confirm_keyboard())
    await state.set_state(UserDeleteState.confirm)


@router.message(StateFilter(UserDeleteState.confirm), F.text == "Ha ✅")
async def send_message(message: types.Message, state: FSMContext):
    data = await state.get_data()
    id = data.get("id")

    user = db.query(User).filter_by(id=id).first()
    db.delete(user)
    db.commit()
    db.close()

    await message.answer("Ma'lumot o'chirildi")
    await state.clear()


@router.message(StateFilter(UserDeleteState.confirm), F.text == "Yo'q ❌")
async def send_message(message: types.Message, state: FSMContext):
    data = await state.get_data()
    id = data.get("id")

    user = db.query(User).filter_by(id=id).first()
    db.delete(user)
    db.commit()
    db.close()

    await message.answer(text="Ortga qaytingiz",
                         reply_markup=back_keyboard())
    await state.clear()
