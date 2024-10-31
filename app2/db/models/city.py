from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app2.db.database import Base


class City(Base):
    __tablename__ = "cities"
    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String)
    country_id = Column(Integer, ForeignKey("countries.country_id"))
    latitude = Column(Float)
    longitude = Column(Float)

    country = relationship("Country", back_populates="cities")
    target = relationship("Target", back_populates="city")
