# %load q02_teams/build.py
# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
def teams(data):
    Nilesh=data['info']['teams']
    return Nilesh
teams(data)


type(data)
data.keys()
data['info']
d=data['info']
type(d)
d.keys()
d['teams']
Nilesh=data['info']['teams']
Nilesh


