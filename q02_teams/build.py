# %load q02_teams/build.py
# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
import pandas as pd
data = read_data()

# solution
def teams(data=data):
    info = data['info']
    teams = info['teams']
    return teams

print(teams(data))






