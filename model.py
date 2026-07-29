from sqlalchemy import Column, Integer, String
from database import Base

class Electronics(Base):
    __tablename__ = "Electronics_1"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    e_type = Column(String(50), nullable=False)
    price=Column(Integer,nullable=False)
    voltage=Column(String(50),nullable=True)


class FootWear(Base):
    __tablename__ = "Foot_wear"

    f_id = Column(Integer, primary_key=True, index=True)
    f_name = Column(String(100), nullable=False)
    size = Column(Integer, nullable=False)
    f_price = Column(Integer, nullable=False)
    company=Column(String(50),nullable=True)
    