from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
from database import Motor


user_collection = Motor(collection="user")


class BanMiddleWare(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                       message: Message,
                       data: Dict[str, Any]) -> Any:
        user = await user_collection.get_user(tg_id=message.from_user.id)
        if user.is_active:
            result = await handler(message, data)
            return result