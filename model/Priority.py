from sqlalchemy import Column, Integer, String

from config.base import Base


class Priority(Base):
    __tablename__ = 'priority'

    id = Column(Integer, primary_key=True)
    priority_level = Column(String(50))