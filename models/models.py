from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy import declarative_base

# Cria a conexão com o banco
db = create_engine("127.0.0.1:3306//banco.db")


# Cria a base do banco de dados
Base = declarative_base()


# Cria as tabelas e classes do banco de dados
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


# Executa a criação do banco de dados
