from aiogram import Router
from aiogram.types import Message
from aiogram import F
from database import Motor, AddUserSchema
from bot.keyboards import start_kb


router = Router()
user_collection = Motor(collection="user")


@router.message(F.text == "/start")
async def start(message: Message):
    await message.answer('sosi'  + message.text)


# @router.message()
# async def echo(message: Message):penis
#     await message.answer('sosi '  + message.text)


@router.message(F.text == "/app")
async def open_webapp(message: Message):
    await message.answer(text='ddd', reply_markup=start_kb)


@router.message(F.text == "/addme")
async def adduser(message: Message):
    user = AddUserSchema(
        username=message.from_user.username,
        tg_id=message.from_user.id,
    )
    await message.answer(text=f'{user.username}')
    add_result = await user_collection.add_user(user)
    await message.answer(text=f"id of user: {add_result}")

    # await user_collection.redis_client.hset(name=f'user:{user.tg_id}', mapping=user.model_dump())

    redis_user = await user_collection.redis_client.hgetall(name=f'user:{message.from_user.id}')
    await message.answer(text=f'username:{redis_user.get('username')}\nis superuser: {redis_user.get('is_superuser')}')

    get_result = await user_collection.get_user(tg_id=message.from_user.id)
    await message.answer(text=f"username: {get_result.username}")
