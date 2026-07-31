import os
from dotenv import load_dotenv

from sqlalchemy import create_engine 
#connection for database

from sqlalchemy.orm import sessionmaker, declarative_base



#http://localhost:8000
load_dotenv()
DATABASE_URL=os.getenv("DB_URL")
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
