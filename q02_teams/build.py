# %load q02_teams/build.py
# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(data=data):
    teams1 = [x[3] for x in ipl[:1]]
    teams2 = [x[4] for x in ipl[:1]]
    team_1=set(teams1)
    team_2=set(teams2)
    teams = [team_1.union[team_2]]

    # write your code here
    #teams =

    return teams



