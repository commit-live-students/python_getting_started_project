import pandas as pd

# %load q02_teams/build.py
# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data

data = read_data()

# solution
def teams(df):
    # write your code here
    teams = df['info']['teams']
    return teams
    
teams(data)





