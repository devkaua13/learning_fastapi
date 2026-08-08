from fastapi import APIRouter, Depends, HTTPException
from models import User
from dependencies import take
from services import bcrypt_context
from schemas import UserSchema
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get("/")
async def auth():
    """
    Essa é a rota padrão de autenticação do nosso sistema
    """
    return {"Mensagem": "Você acessou a rota de autenticação"}


@auth_router.post("/create-users")
async def create_users(user_schema: UserSchema, session: Session = Depends(take)):
    user = session.query(User).filter(User.email == user_schema.email).first()
    if user:
        # raise é para estourar o erro
        raise HTTPException(status_code=400, detail="User exists")
    else:
        password_crypt = bcrypt_context.hash(user_schema.password)
        new_user = User(
            user_schema.name,
            user_schema.email,
            password_crypt,
            user_schema.active,
            user_schema.is_admin,
        )
        session.add(new_user)
        session.commit()
        return {"message": "User succesfull created {user_schema.email}"}
