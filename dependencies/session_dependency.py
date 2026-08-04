from sqlalchemy.orm import sessionmaker
from models import db


def take():
    session = None
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        if session is not None:
            session.close()
