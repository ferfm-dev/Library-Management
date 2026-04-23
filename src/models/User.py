from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(75))

    loans = relationship("Loan", back_populates="user")