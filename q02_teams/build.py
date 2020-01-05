# %load q02_teams/build.py
# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(data=data):

    # write your code here
    teams = data['info']['teams']

    print(type(teams))
    
    return teams

from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

teams = data['info']['teams']
type(teams)
type(data)
teams[1]
teams
for i in teams:
    print(i)
len(teams)
teams.append('Crack Commandoes')
for k in teams:
    print(k)
teams.insert(2,'Baja')
for j in teams:
    print(j)
teams.pop()
teams
teams.reverse()
for i in teams: print(i)
del teams[0]
teams

teams.reverse()
teams


