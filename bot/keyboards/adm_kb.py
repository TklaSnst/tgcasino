from aiogram.types import InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton, WebAppInfo
import os

adm_main_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="ban_user", callback_data="")],
    [InlineKeyboardButton(text="get_user", callback_data="")],
    [InlineKeyboardButton(text="return", callback_data="")]
])
