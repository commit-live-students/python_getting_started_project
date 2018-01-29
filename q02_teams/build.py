# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(data=data):
    teams = []
    for rec in  data.item():
        if rec[0] ='info' and rec[1]='teams':
            teams = teams.append [rec]
    return teams
