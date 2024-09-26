from sqlalchemy import Column, Integer, String

from config.base import Base


class TargetType(Base):
    __tablename__ = 'target_type'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type_name = Column(String(255), unique=True,nullable=False)