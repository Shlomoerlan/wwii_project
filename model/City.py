
class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    city_name = Column(String(255))
    country_id = Column(Integer, ForeignKey('country.id'))

    # הגדרת קשר עם טבלת country
    country = relationship("Country")