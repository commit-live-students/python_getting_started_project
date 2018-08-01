# %load q02_teams/build.py
# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(data=data):
    team_1 = []
    team_2 = []
    for x in data[1:]:
        team_1.append(x[3])
    for x in data[1:]:
        team_2.append(x[4])
    team_1 = set(team_1)
    team_2 = set(team_2)
    teams = (team_1.union(team_2))

    return teams



