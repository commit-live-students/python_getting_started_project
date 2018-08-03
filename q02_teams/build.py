# %load q02_teams/build.py
# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(data=data):

    # write your code here
    #teams =

    return teams

data = read_data()
def teams(info):
    teams = []
    for x in data['info']['teams']:
        #if x[0] == info:
            teams.append(x)
    return teams

  #  info = {teams:info}
print(data['info']['teams'])
teams('info')




