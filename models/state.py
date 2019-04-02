#!/usr/bin/python3
"""This is the state class"""

import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    @property
    def cities(self):
        """Returns the list of City instances with equal state_id"""
        cities = storage.all(City)
        self.__cities = [city for city in cities if city.state_id == self.id]
        return self.__cities
