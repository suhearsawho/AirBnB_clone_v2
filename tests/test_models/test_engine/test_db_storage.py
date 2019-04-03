#!/usr/bin/python3

import unittest
import pep8
from models import Amenity
from models import State
from models import City
from models import Place
from models import User
from models import Review
from models.engine.db_storage import DBStorage
from os import environ


class TestDBStorage(unittest.TestCase):
    """Tests the DBStorage class"""

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        """
        environ['HBNB_ENV'] = 'test'
        environ['HBNB_MYSQL_USER'] = 'hbnb_test'
        environ['HBNB_MYSQL_PWD'] = 'hbnb_test_pwd'
        environ['HBNB_MYSQL_HOST'] = 'localhost'
        environ['HBNB_MYSQL_DB'] = 'hbnb_test_db'
        environ['HBNB_TYPE_STORAGE'] = 'db'
        """
        pass

    @unittest.skipIf('HBNB_TYPE_STORAGE' not in environ or
                     environ['HBNB_TYPE_STORAGE'] != 'db', 'These tests\
                     should only be used when storage type is db')
    def setUp(self):
        """Setup the class"""
        self.user = User()
        self.user.first_name = "Kev"
        self.user.last_name = "Yo"
        self.user.email = "1234@yahoo.com"
        self.user.password = "1234"
        self.storage = DBStorage()
        self.storage.reload()

    def tearDownClass():
        """
        del environ['HBNB_ENV']
        del environ['HBNB_MYSQL_USER']
        del environ['HBNB_MYSQL_PWD']
        del environ['HBNB_MYSQL_HOST']
        del environ['HBNB_MYSQL_DB']
        del environ['HBNB_TYPE_STORAGE']
        """
        pass

    @unittest.skipIf('HBNB_TYPE_STORAGE' not in environ or
                     environ['HBNB_TYPE_STORAGE'] != 'db', 'These tests\
                     should only be used when storage type is db')
    def test_all(self):
        """ Tests db_storage all method to query objects in the database
        """
        original_len = self.storage.all(User)
        self.storage.new(self.user)
        self.storage.save()
        new_len = self.storage.all(User)
        self.assertTrue(original_len != new_len)

    @unittest.skipIf('HBNB_TYPE_STORAGE' not in environ or
                     environ['HBNB_TYPE_STORAGE'] != 'db', 'These tests\
                     should only be used when storage type is db')
    def test_new(self):
        """ Tests db_storage new method to add a new object"""
        original_len = self.storage.all(User)
        self.storage.new(self.user)
        self.storage.save()
        new_len = self.storage.all(User)
        self.assertTrue(original_len != new_len)

    @unittest.skipIf('HBNB_TYPE_STORAGE' not in environ or
                     environ['HBNB_TYPE_STORAGE'] != 'db', 'These tests\
                     should only be used when storage type is db')
    def test_save(self):
        """ Tests db_storage save method to save the added object """
        original_len = self.storage.all(User)
        self.storage.new(self.user)
        self.storage.save()
        new_len = self.storage.all(User)
        self.assertTrue(original_len != new_len)

    @unittest.skipIf('HBNB_TYPE_STORAGE' not in environ or
                     environ['HBNB_TYPE_STORAGE'] != 'db', 'These tests\
                     should only be used when storage type is db')
    def test_delete(self):
        """ Tests db_storage delete method to delete an object form the db
        """
        original_len = self.storage.all(User)
        self.storage.new(self.user)
        self.storage.save()
        self.storage.delete(self.user)
        new_len = self.storage.all(User)
        self.assertTrue(original_len == new_len)

    @unittest.skipIf('HBNB_TYPE_STORAGE' not in environ or
                     environ['HBNB_TYPE_STORAGE'] != 'db', 'These tests\
                     should only be used when storage type is db')
    def test_reload(self):
        """Tests db_storage delete method"""
        pass
    """def test_reload(self):
    Should we do this?
    Also I think we should delete the commits on both new and delete """
