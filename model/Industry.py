from sqlalchemy import Column, Integer, String
from config.base import Base


class Industry(Base):
    __tablename__ = 'industry'

    id = Column(Integer, primary_key=True, autoincrement=True)
    industry_name = Column(String(255), unique=True, nullable=False)