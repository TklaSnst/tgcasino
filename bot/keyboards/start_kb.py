from aiogram.types import InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton, WebAppInfo

start_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="open",
                              web_app=WebAppInfo(url="https://vertically-top-cat.ngrok-free.app/page/main/"))],
        [InlineKeyboardButton(text="another...", callback_data="open_smthng")]
])
