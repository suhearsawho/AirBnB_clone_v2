#!/usr/bin/python3
"""test for place"""
import unittest
import os
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.user import User
from models.base_model import BaseModel
import pep8


class TestPlace(unittest.TestCase):
    """this will test the place class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        from models import storage

        cls.state = State(name="California")
        cls.city = City(name="Los Angeles", state_id=cls.state.id)
        cls.user = User(email="john@snow.com", password="johnpwd")
        cls.amenity = Amenity(name="Television")
        cls.place = Place(city_id=cls.city.id, state_id=cls.state.id,
                          name='Death Star', user_id=cls.user.id,
                          description='Unlimited power', number_rooms=12,
                          number_bathrooms=12, max_guest=12, price_by_night=12,
                          latitude=10.0, longitude=12.0,
                          )

        if ('HBNB_TYPE_STORAGE' in os.environ and
                os.environ['HBNB_TYPE_STORAGE'] == 'db'):
            cls.place.amenities.append(cls.amenity)
        else:
            cls.place.amenities = cls.amenity

        storage.new(cls.state)
        storage.new(cls.city)
        storage.new(cls.user)
        storage.new(cls.amenity)
        storage.new(cls.place)

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.place
        del cls.city
        del cls.amenity
        del cls.state
        del cls.user

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Place(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_Place(self):
        """checking for docstrings"""
        self.assertIsNotNone(Place.__doc__)

    def test_attributes_Place(self):
        """chekcing if amenity have attributes"""
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)

    def test_is_subclass_Place(self):
        """test if Place is subclass of Basemodel"""
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_attribute_types_Place(self):
        """test attribute type for Place"""
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_save_Place(self):
        """test if the save works"""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_to_dict_Place(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.place), True)

    @unittest.skipIf('HBNB_TYPE_STORAGE' in os.environ and
                     os.environ['HBNB_TYPE_STORAGE'] == 'db',
                     'getter attribute will overwrite sqlalchemy protocols')
    def test_place_review_getter(self):
        """Tests the reviews getter attribute when file storage is used"""
        from models import storage
        from models import Review
        reviews = storage.all(Review)
        actual = [reviews for review in reviews
                  if review.place_id == self.place.id]
        expected = self.place.reviews
        self.assertEqual(expected, actual)
        self.assertEqual(list, type(actual))


if __name__ == "__main__":
    unittest.main()
