# %load q02_teams/build.py
# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(match_data):

    # write your code here
    #teams =

    return match_data['info']['teams']
print(teams(data))



