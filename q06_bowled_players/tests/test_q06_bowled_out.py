import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from q06_bowled_players.build import bowled_out
from greyatomlib.python_getting_started.q01_read_data.build import read_data

data = read_data()
bowled_out_players = bowled_out(data)
class TestBowled_out(TestCase):
    def test_bowled_out_return_type(self):
        
        self.assertIsInstance(bowled_out_players, list,"The Expected type does not match return type")

    def test_bowled_out_return_value(self):
        self.assertSetEqual(set(bowled_out_players), set(['R Dravid', 'V Kohli', 'Z Khan']),"The Expected Value does not match return value")
