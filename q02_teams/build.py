# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(data=data):
    teams = []
    # write your code here
    for key in data:
        if key == 'info':
            teams = data['info']['teams']
    return teams
