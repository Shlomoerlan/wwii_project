from sqlalchemy import Column, Integer, Numeric, UniqueConstraint
from config.base import Base


class Target(Base):
    __tablename__ = 'target'

    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Numeric)
    longitude = Column(Numeric)

    __table_args__ = (UniqueConstraint('latitude', 'longitude', name='unique_lat_long'),)

