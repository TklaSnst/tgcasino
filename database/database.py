import os
from typing import Any, Dict
from database import AddUserSchema, GetUserSchema
from redis.asyncio import Redis
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi


url = "172.17.0.1"
db = "bot"


class Motor:
    def __init__(self, collection: str, cache: bool = True):
        """
        Инициальзация подключения к Mongodb
        :param collection: Название коллекции
        :param cache:
        """
        self.client = AsyncIOMotorClient(
            host='172.17.0.1',
            port=27017,
            username=os.getenv("MONGODB_ROOT_USERNAME"),
            password=os.getenv("MONGODB_ROOT_PASSWORD")
        )
        self.db = self.client[db]
        self.collection = self.db[collection]
        self.cache = cache
        if cache:
            self.redis_client = Redis(host='172.17.0.1', port=6379, db=0, decode_responses=True)

    async def add_user(self, user: AddUserSchema) -> str | None:
        """
        Вставка одного пользователя в коллекцию.
        :user: пользователь для вставки.
        :return: ID вставленного пользователя.
        """
        if self.collection.find_one({"username": user.username}):
            return "user is already exists"

        result = await self.collection.insert_one(*user)

        async with self.redis_client as redis:
            pipe = redis.pipeline()
            await pipe.hset(name=f'user:{user.tg_id}', mapping=user.model_dump())
            await pipe.expire(f'user:{user.tg_id}', 500)
            await pipe.execute()

        return str(result.inserted_id)

    async def get_user(self, tg_id: int) -> GetUserSchema | None:
        async with self.redis_client as redis:
            redis_user = await redis.hgetall(name=f'user:{tg_id}')
            if not redis_user:
                user = await self.collection.find_one({"tg_id": tg_id})
                if not user:
                    return None
                pipe = redis.pipeline()
                await pipe.hset(name=f'user:{tg_id}', mapping=dict(user))
            return GetUserSchema(**redis_user)
