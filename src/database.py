from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///database/library.db"

Base = declarative_base()

def get_engine(db_url=DATABASE_URL):
    engine = create_engine(DATABASE_URL, echo=False)

    return engine

def create_tables(engine):
    Base.metadata.create_all(engine)

def get_session(engine):
    Session = sessionmaker(bind=engine)
    
    return Session()