from aiogram.types import CallbackQuery, Message
from bot.keyboards import adm_main_kb
from aiogram import Router
from aiogram import F


router = Router()


@router.callback_query(F.data == "admin_panel")
async def adm_panel_main(callback: CallbackQuery):
    await callback.message.answer(text="Ok, here's some options...", reply_markup=adm_main_kb)
