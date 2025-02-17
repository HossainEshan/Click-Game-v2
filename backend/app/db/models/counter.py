from sqlalchemy import Column, Integer
from app.db.base import Base

class Counter(Base):
    __tablename__ = "counter"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Integer, default=0)