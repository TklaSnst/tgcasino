from aiogram import Router
from aiogram.types import Message
from aiogram import F


router = Router()


@router.message(F.text == "/start")
async def start(message: Message):
    await message.answer('sosi'  + message.text)

@router.message()
async def echo(message: Message):
    await message.answer('sosi '  + message.text)

