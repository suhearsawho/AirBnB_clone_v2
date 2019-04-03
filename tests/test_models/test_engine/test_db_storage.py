#!/usr/bin/python3

import unittest
from models import Amenity
from models import State
from models import City
from models import Place
from models import User
from models import Review

class TestDBStorage(unittest.TestCase):
    """Tests the DBStorage class"""
    
    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_
