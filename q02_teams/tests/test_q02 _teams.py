import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))

from unittest import TestCase
from greyatomlib.python_getting_started.q01_read_data.build import read_data
from q02_teams.build import teams

data = read_data()
ipl_teams = teams(data)

class TestTeams(TestCase):
    def test_teams_return_type(self):
        self.assertIsInstance(ipl_teams, list,"Expected type does not match the return type")

    def test_teams_return_Royal_Challengers(self):
        self.assertTrue('Royal Challengers Bangalore' in ipl_teams,"Expected team does not match with the return team")

    def test_teams_return_Knight_Riders(self):
        self.assertTrue('Kolkata Knight Riders' in ipl_teams,"Expected team does not match with the return team")

    def test_teams_return_number_of_teams(self):
        self.assertEqual(len(ipl_teams),2,"The expected number of teams does not ")
