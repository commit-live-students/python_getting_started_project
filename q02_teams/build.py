# %load q02_teams/build.py
# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
lst = []

def teams(data):
    lst.append(data['info']['teams'])
    # write your code here
        
    return lst[0]

teams(data)
lst[0]

