from sqlalchemy import Column, Integer, DateTime ,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, UTC
from src.database import Base

class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))

    borrowed_at = Column(DateTime, default=lambda: datetime.now(UTC), nullable=False)
    due_date = Column(DateTime, nullable=False)
    returned_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="loans")
    book = relationship("Book", back_populates="loans")