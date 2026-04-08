import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.models import Base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine) 

def init_db():
    Base.metadata.create_all(bind=engine)
    print ("Banco de dados inicializado com sucesso!")

def get_session():
    return SessionLocal()

