import unittest

from ccpin import valid_input, main

class PinTest(unittest.TestCase):

    def test_get_correct_input(self):
        self.assertTrue(valid_input("1234"))

    def test_get_long_input(self):
        self.assertFalse(valid_input("12344567"))

    def test_get_short_input(self):
        self.assertFalse(valid_input("123"))

    def test_get_alpha_input(self):
        self.assertFalse(valid_input("12AB"))


