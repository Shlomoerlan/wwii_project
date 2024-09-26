from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from config.base import Base


class NewMission(Base):
    __tablename__ = 'new_mission'

    id = Column(Integer, primary_key=True, autoincrement=True)
    target_id = Column(Integer, ForeignKey('target.id'))
    country_id = Column(Integer, ForeignKey('country.id'))
    city_id = Column(Integer, ForeignKey('city.id'))
    industry_id = Column(Integer, ForeignKey('industry.id'))
    type_id = Column(Integer, ForeignKey('target_type.id'))
    priority_id = Column(Integer, ForeignKey('priority.id'))

    target = relationship("Target")
    country = relationship("Country")
    city = relationship("City")
    industry = relationship("Industry")
    target_type = relationship("TargetType")
    priority = relationship("Priority")
