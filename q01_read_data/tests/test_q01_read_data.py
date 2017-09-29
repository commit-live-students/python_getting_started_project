import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))

from unittest import TestCase
from q01_read_data.build import read_data

class TestRead_data(TestCase):
    def test_read_data(self):
        result = read_data()
        self.assertIsInstance(result, dict)
