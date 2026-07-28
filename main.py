from fastapi import FastAPI

app = FastAPI()


from routes import auth_router, order_router

app.include_router(auth_router)
app.include_router(order_router)
# Comando para rodar com uvicorn - uv run uvicorn main:app --reload
