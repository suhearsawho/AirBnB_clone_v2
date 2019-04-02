#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import environ


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             nullable=False, primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             nullable=False, primary_key=True)
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
    amenities = relationship(
        'Amenity', secondary=place_amenity, viewonly=False)
    reviews = relationship('Review', cascade='all, delete', backref='place')

    @property
    def reviews(self):
        """Getter function for reviews"""
        from models import Review
        from models import storage
        reviews = storage.all(Review)
        self.__reviews = [review for review in reviews.values()
                          if review.place_id == self.id]
        return self.__reviews

    @property
    def amenities(self):
        """Getter function for amenities"""
        from models import Amenity
        from models import storage
        amenities = storage.all(Amenity)
        self.__amenities = [amenity for amenity in amenities.values()
                            if amenity.place_amenities.place_id == self.id]
        return self.__amenities

    @amenities.setter
    def amenities(self, obj=None):
        """Setter function for amenities"""
        from models import Amenity
        from models import storage
        if type(obj) == Amenity:
            amenity_ids.append(obj.id)
