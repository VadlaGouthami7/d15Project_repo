from sqlalchemy import create_engine 
#connection for database

from sqlalchemy.orm import sessionmaker, declarative_base


# DATABASE_URL = "mysql+pymysql://root:gouthami%405f7@localhost:3306/project_db"
#http://localhost:8000
DATABASE_URL="mysql+pymysql://avnadmin:AVNS_Sc8fGmoHJQT-PEmh3pb@gouthami-7-gouthamivadla7-5fb0.j.aivencloud.com:28983/defaultdb"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
