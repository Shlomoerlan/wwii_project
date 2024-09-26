from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.base import Base


class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String(255), unique=True, nullable=False)
    country_id = Column(Integer, ForeignKey('country.id'), unique=True, nullable=False)

    country = relationship("Country")
