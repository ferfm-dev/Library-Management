"""
RUN THIS SCRIPT FIRST!!!
"""

from src.database import get_engine, create_tables
from src.models import User, Book, Loan

def setup_database():

    engine = get_engine()
    create_tables(engine)

    print("Database and tables created successfully!")

if __name__ == "__main__":
    setup_database()