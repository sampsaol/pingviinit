import unittest
from util import validate_year
from datetime import datetime

class Test_articleyear(unittest.TestCase):
    def setUp(self):
        pass

    def test_positive_year(self):
        self.assertTrue(validate_year(2023))

    def test_zero_year(self):
        with self.assertRaises(ValueError, msg="Vuoden on oltava positiivinen"):
            validate_year(0)

    def test_negative_year(self):
        with self.assertRaises(ValueError, msg="Vuoden on oltava positiivinen"):
            validate_year(-100)

    def test_one(self):
        self.assertTrue(validate_year(1))

    def test_future(self):
        current_year = datetime.now().year

        self.assertTrue(validate_year(current_year))
        with self.assertRaises(ValueError, msg="Vuosi ei voi olla tulevaisuudessa"):
            validate_year(current_year + 1)


