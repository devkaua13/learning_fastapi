from sqlalchemy import create_engine
from sqlalchemy import declarative_base

# Cria a conexão com o banco
db = create_engine("127.0.0.1:3306//banco.db")


# Cria a base do banco de dados
base = declarative_base()

# Cria as tabelas e classes do banco de dados


# Executa a criação do banco de dados
