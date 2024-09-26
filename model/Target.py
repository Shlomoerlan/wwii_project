from sqlalchemy import Column, Integer, Numeric
from config.base import Base


class Target(Base):
    __tablename__ = 'target'

    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Numeric, unique=True)
    longitude = Column(Numeric, unique=True)


