# %load q02_teams/build.py
# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(data=data):
    x=[]
    x=data['info']['teams']
    
    return x

a=teams(data)
a


