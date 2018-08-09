# %load q02_teams/build.py
# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(data=data):
    y= data['info']['teams']
    # with open('ipl_match.yaml', 'r') as f:
    # write your code here
    #teams =

    return y
teams()

