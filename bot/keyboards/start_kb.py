from aiogram.types import InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton, WebAppInfo
import os


start_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="open",
                              web_app=WebAppInfo(url="https://vertically-top-cat.ngrok-free.app/page/main/"))],
        [InlineKeyboardButton(text="another...", callback_data="open_smthng")]
])


adm_start_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="open",
                              web_app=WebAppInfo(url="https://vertically-top-cat.ngrok-free.app/page/main/"))],
        [InlineKeyboardButton(text="admin_panel", callback_data="admin_panel")]
])


async def get_start_kb(tg_id: int):
    if tg_id != int(os.getenv("ADM_TG_ID")):
        return start_kb
    return adm_start_kb
