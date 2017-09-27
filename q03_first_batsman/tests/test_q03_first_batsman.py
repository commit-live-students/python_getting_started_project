import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..', '..'))
from unittest import TestCase
from q01_read_data.build import read_data
from q03_first_batsman.build import first_batsman

class TestFirst_batsman(TestCase):
    def test_first_batsman(self):
        data = read_data()
        batsman_name = first_batsman(data)
        self.assertIsInstance(batsman_name, str)
        self.assertTrue('SC Ganguly' == batsman_name)
