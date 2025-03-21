from pydantic import BaseModel, Field


class AddUserSchema(BaseModel):
    tg_id: int
    username: str = Field(max_length=50)
    balance: int = Field(default=100)
    is_superuser: int = Field(default=0, ge=0, le=1)
    is_active: int = Field(default=1, ge=0, le=1)
    jwt_refresh_token: str = Field(default="")


class GetUserSchema(AddUserSchema):
    pass
