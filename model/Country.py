from sqlalchemy import Column, Integer, String
from config.base import Base


class Country(Base):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True, autoincrement=True)
    country_name = Column(String(255), unique=True, nullable=False)