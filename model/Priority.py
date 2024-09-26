from sqlalchemy import Column, Integer, String

from config.base import Base


class Priority(Base):
    __tablename__ = 'priority'

    id = Column(Integer, primary_key=True, autoincrement=True)
    priority_level = Column(String(50), unique=True, nullable=False)