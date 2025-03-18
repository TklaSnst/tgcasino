from aiogram import Router
from aiogram.types import Message
from aiogram import F
from bot.keyboards import start_kb


router = Router()


@router.message(F.text == "/start")
async def start(message: Message):
    await message.answer('sosi'  + message.text)


# @router.message()
# async def echo(message: Message):
#     await message.answer('sosi '  + message.text)


@router.message(F.text == "/app")
async def open_webapp(message: Message):
    await message.answer(text='ddd', reply_markup=start_kb)
