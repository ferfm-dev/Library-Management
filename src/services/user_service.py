from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.models.User import User

def create_user(session: Session, name: str) -> User:
    if not name or not name.strip():
        raise ValueError("User name can not be empty.")
    
    user = User(name=name.strip())

    try:
        session.add(user)
        session.commit()
        session.refresh(user)
        
        return user
    except SQLAlchemyError as e:
        session.rollback()
        raise Exception("Create User Error:", e)

def get_user_by_id(session: Session, user_id: int) -> User:
    user = session.get(User, user_id)

    if not user:
        raise ValueError(f"User ID {user_id} not found.")

    return user

def list_users(session: Session) -> list[User]:
    return session.query(User).all()

def delete_user(session: Session, user_id: int) -> None:
    user = session.get(User, user_id)

    try:
        session.delete(user)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        raise Exception(f"Error {e} to delete User {user_id}")