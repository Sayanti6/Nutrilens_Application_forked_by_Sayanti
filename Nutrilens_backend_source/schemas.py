from pydantic import BaseModel, EmailStr, Field

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: str | None = None


class User(BaseModel):
    username: str
    email: EmailStr | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    # id: str = Field(alias="_id") means
    # "When data contains '_id', store it inside field named 'id'"
    id: str = Field(alias="_id")
    hashed_password: str

class UserModelDB(User):
    hashed_password: str

class RegisterUserForm(BaseModel):
    username: str
    email: EmailStr | None = None
    password: str = Field(min_length=8)
    full_name: str | None = None


# class Register(BaseModel):
#     name: str
#     username: str
#     password: str
#     role: str
#     contact: str

# class RegisterForm(Register):
#     confirmPassword: str

class LoginForm(BaseModel):
    username: str
    password: str

class VerifiedUser(BaseModel):
    name: str
    username: str
    role: str

