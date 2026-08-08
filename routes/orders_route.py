from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Order
from schemas import OrderSchema
from dependencies import take

order_router = APIRouter(prefix="/orders", tags=["order"])


@order_router.get("/")
async def orders():
    return {"Mensagem": "Você acessou a rota depedidos"}


@order_router.post("/order")
async def create_order(order_schema: OrderSchema, session: Session = Depends(take)):
    new_order = Order(user=order_schema.id_user)
    session.add(new_order)
    session.commit()
    return {"mensagem": "Order created successfull {new_order.id}"}
