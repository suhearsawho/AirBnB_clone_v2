#!/usr/bin/python3
"""This defines the DBStorage class"""
import sqlalchemy
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from os import environ

# TODO When do we close the session? Does the session close?


class DBStorage():
    """Defines the DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Defines setup for DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      environ['HBNB_MYSQL_USER'],
                                      environ['HBNB_MYSQL_PWD'],
                                      environ['HBNB_MYSQL_HOST'],
                                      environ['HBNB_MYSQL_DB'],
                                      pool_pre_ping=True))
        if "HBNB_ENV" in environ and environ['HBNB_ENV'] == 'test':
            Session = sessionmaker(bind=self.__engine)
            self.__session = Session()
            for table in reversed(Base.meta.sorted_tables):
                engine.execute(tbl.delete())
            self.__session.close()

    def all(self, cls=None):
        """Performs a query on the current database session"""
        object_types = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']

        object_dict = {}

        if cls is None:
            for my_type in object_types:
                query = self.__session.query(my_type).all()
                for obj in query:
                    key = obj.__class__.__name__ + '.' + obj.id
                    object_dict[key] = obj
        else:
            query = self.__session.query(cls).all()
            for obj in query:
                key = obj.__class__.__name__ + '.' + obj.id
                object_dict[key] = obj

        return object_dict

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)
        self.__session.commit()

    def save(self):
        """Commits all changes fo the current database session"""
        self.__session.commit()
        self.__session.close()

    def delete(self, obj=None):
        """Deletes obj from current database session if not None"""
        if obj:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        """Creates all tables in the database"""
        Base.metadata.create_all(bind=self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
