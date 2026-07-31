from enum import auto
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    Float,
)
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

# Cria a conexão com o banco
db = create_engine("127.0.0.1:3306//learning.db")


# Cria a base do banco de dados
Base = declarative_base()


# Cria as tabelas e classes do banco de dados

# User


class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    email = Column("email", String, nullable=False)
    password = Column("password", String)
    active = Column("active", Boolean)
    is_admin = Column("is_admin", Boolean, default=False)

    def __init__(self, name, email, password, active=True, is_admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.is_admin = is_admin


# Order


class Order(Base):
    __tablename__ = "orders"

    STATUS_PEDIDOS = (
        ("PENDING", "PENDING"),
        ("FINISH", "FINISH"),
        ("CANCELLED", "CANCELLED"),
    )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column(
        "status", ChoiceType(choices=STATUS_PEDIDOS)
    )  # FINISH, CANCELLED, PENDING
    user = Column("user", ForeignKey("users.id"))
    price = Column("price", Float)

    def __init__(self, user, status="PENDING", price=0):
        self.user = user
        self.status = status
        self.price = price


# ItemOrder


class OrderItem(Base):
    __table__ = "orderitems"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantity = Column("quantity", Integer)
    flavor = Column("flavor", String)
    bulk = Column("bulk", String)
    unit_price = Column("unit_proce", Float)
    order = Column("order", ForeignKey("orders.id"))

    def __init__(self, quantity, flavor, bulk, unit_price, order):
        self.quantity = quantity
        self.flavor = flavor
        self.bulk = bulk
        self.unit_price = unit_price
        self.order = order


# Executa a criação do banco de dados
