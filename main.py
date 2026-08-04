from fastapi import FastAPI
from routes import auth_router, order_router
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

app.include_router(auth_router)
app.include_router(order_router)
# Comando para rodar com uvicorn - uv run uvicorn main:app --reload
