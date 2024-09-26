


class Country(Base):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True)
    country_name = Column(String(255), unique=True)