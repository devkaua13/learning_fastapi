from sqlalchemy.orm import sessionmaker
from models import db


def take():
    Session = sessionmaker(bind=db)
    session = Session()
    yield session
    session.close()
