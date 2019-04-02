#!/usr/bin/python3
"""This is the amenity class"""
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, String
from models.place import place_amenity


class Amenity(BaseModel):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
