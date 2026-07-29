from sqlalchemy import create_engine 
#connection for database

from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "mysql+pymysql://root:gouthami%405f7@localhost:3306/project_db"
#http://localhost:8000
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()