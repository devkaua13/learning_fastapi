from fastapi import APIRouter, Depends
from models import User
from dependencies import take
from services import bcrypt_context

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get("/")
async def auth():
    """
    Essa é a rota padrão de autenticação do nosso sistema
    """
    return {"Mensagem": "Você acessou a rota de autenticação"}


@auth_router.post("/create-users")
async def create_users(email: str, password: str, name: str, session=Depends(take)):
    user = session.query(User).filter(User.email == email).first()
    if user:
        return {"message": "User exists"}
    else:
        password_crypt = bcrypt_context.hash(password)
        new_user = User(name, email, password_crypt)
        session.add(new_user)
        session.commit()
        return {"message": "User succesfull created"}
