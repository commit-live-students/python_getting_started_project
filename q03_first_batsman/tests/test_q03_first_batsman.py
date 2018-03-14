import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from greyatomlib.python_getting_started.q01_read_data.build import read_data
from q03_first_batsman.build import first_batsman

data = read_data()
batsman_name = first_batsman(data)


class TestFirst_batsman(TestCase):
    def test_first_batsman_return_type(self):
        self.assertIsInstance(batsman_name, str)

    def test_first_batsman_return_value(self):
        self.assertEqual('SC Ganguly', batsman_name, "The Expected name does not match with the returned name")