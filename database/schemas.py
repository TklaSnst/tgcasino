from pydantic import BaseModel, Field


class AddUserSchema(BaseModel):
    tg_id: int
    username: str = Field(max_length=50)
    balance: int = Field(default=100)
    is_superuser: bool = Field(default=False)
    is_active: bool = Field(default=True)
    jwt_refresh_token: str | None = Field(default=None)


class GetUserSchema(AddUserSchema):
    pass
