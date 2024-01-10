from pydantic import BaseModel, Field

# Модель для хранения пользователя
class User(BaseModel):
    user_id: int
    role: int
    user_name: str = Field(min_length=2)
    user_surname: str = Field(min_length=2)
    user_age: int
    user_nickname: str = Field(min_length=3)