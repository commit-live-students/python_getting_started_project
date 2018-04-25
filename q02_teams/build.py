# %load q02_teams/build.py
# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(data=data):
    teams=[]
    for key,element in data.items():
        for e in element:
            if type(e) is dict:
                for key1,element1 in e.items():
                    teams.append(element1['team'])
                    

    # write your code here
    #teams =

    return teams



