# %load q02_teams/build.py
# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
print()
# solution
def teams(data=data):
#     data['info']=
#     header=tuple(data[0])
#     team_Royal_Challengers =[x[3] for x in data[1:]] 
#     team_Knight_Riders=[x[4] for x in data[1:]]
#     team_Royal_Challengers=set(team_Royal_Challengers) 
#     team_Knight_Riders=set(team_Knight_Riders)
#     teams=team_Royal_Challengers.union(team_Knight_Riders)
    teams = data['info']['teams']
    return teams

# retrive teams
# set 
# for
# union



