import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..', '..'))
from unittest import TestCase
from q06_bowled_players.build import bowled_out
from q01_read_data.build import read_data
class TestBowled_out(TestCase):
    def test_bowled_out(self):
        data = read_data()
        bowled_out_players = bowled_out(data)
        self.assertIsInstance(bowled_out_players, list)
        self.assertSetEqual(set(bowled_out_players), set(['R Dravid', 'V Kohli', 'Z Khan']))
