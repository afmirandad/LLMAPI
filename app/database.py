from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Config.database import get_database_connection

engine = get_database_connection()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
