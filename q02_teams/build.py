# %load q02_teams/build.py
# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(data):

    # write your code here
    print(data['info']['teams'])

    return teams

teams(data)



