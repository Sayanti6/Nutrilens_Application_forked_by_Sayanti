from fastapi import FastAPI

from Nutrilens_backend_source.routers.authentication import register, login
from Nutrilens_backend_source.routers.user_operations import get_user

app = FastAPI()

app.include_router(register.router)
app.include_router(login.router)
app.include_router(get_user.router)