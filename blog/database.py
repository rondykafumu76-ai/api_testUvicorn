from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

Password = quote_plus("@Jesuis12345")   
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://postgres:{Password}@localhost:5432/produit"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)