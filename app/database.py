from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
'''
DATABASE
'''
# Database
DATABASE_UAL = "sqlite:///./todos.db"
Base = declarative_base()
engine = create_engine(DATABASE_UAL, connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
