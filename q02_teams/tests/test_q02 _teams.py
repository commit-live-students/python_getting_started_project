import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))

from unittest import TestCase
from greyatomlib.python_getting_started.q01_read_data.build import read_data
from q02_teams.build import teams


class TestTeams(TestCase):
    def test_teams(self):
        data = read_data()
        ipl_teams = teams(data)
        self.assertIsInstance(ipl_teams, list)
        self.assertTrue('Royal Challengers Bangalore' in ipl_teams)
        self.assertTrue('Kolkata Knight Riders' in ipl_teams)
        self.assertTrue(len(ipl_teams) == 2)
