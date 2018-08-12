# %load q02_teams/build.py
# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
#print(data['info']['teams'])
# solution
def teams(data=data):

    # write your code here
    teams =data['info']['teams']

    return teams
