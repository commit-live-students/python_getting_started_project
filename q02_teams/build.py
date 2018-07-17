# %load q02_teams/build.py
# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(data=data):
    data = read_data()
    # write your code here
    teams = data['info']['teams']

    return teams

data = read_data()
print(type(data))
print(data['info']['teams'])
#a =data[0]


