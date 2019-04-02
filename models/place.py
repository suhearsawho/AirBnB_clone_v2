#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, ForeignKey, Float
form sqlalchemy.orm import relationship
from os import environ


place_amenity= Table(
        'place_amenity', Base.metadata,
        Column('place_id', ForeignKey('places.id'),
            String(60), nullable=False, primary_key=True),
        Column('amenity_id', ForeignKey('amenities.id'),
            String(60), nullable=False, primary_key=True)
        )

class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    number_rooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    @property
    def reviews(self):
        reviews = storage.all(self)
        rev_li = [ review for review in reviews if review.place_id == self.id ]
        return rev_li

    if 'HBNB_TYPE_STORAGE' in environ and\
            environ['HBNB_TYPE_STORAGE'] == 'db':
                amenties = relationship('Amenity', secondary='place_amenity',
                        viewonly=False)
    else:
        return self.reviews()
