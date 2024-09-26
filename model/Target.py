from sqlalchemy import Column, Integer, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Target(Base):
    __tablename__ = 'target'

    id = Column(Integer, primary_key=True)
    latitude = Column(Numeric)
    longitude = Column(Numeric)


