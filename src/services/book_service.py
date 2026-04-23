from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.models import Book

def create_book(session: Session, title: str) -> Book:
    if not title or not title.strip():
        raise ValueError("Book title can not be empty.")

    book = Book(title=title.title())

    try:
        session.add(book)
        session.commit()
        session.refresh(book)

        return book
    except SQLAlchemyError as e:
        raise Exception("Create Book Error:", e)
    
def get_book_by_id(session: Session, book_id: int) -> Book:
    book = session.get(Book, book_id)

    if not book:
        raise ValueError(f"Book ID {book_id} not found.")
    
    return book

def list_books(session: Session) -> list[Book]:
    return session.query(Book).all()

def delete_book(session: Session, book_id: int) -> None:
    book = session.get(Book, book_id)

    try:
        session.delete(book)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        raise Exception("Error:", e)