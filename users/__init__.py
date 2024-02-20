from pydantic import BaseModel


# Валидатор для регистрации
class UserRegistrationValidator(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str
    password: str
    city: str


# Валидатор для изменении данных пользователя
class EditUserValidator(BaseModel):
    user_id: int
    edit_info: str
    new_info: str
