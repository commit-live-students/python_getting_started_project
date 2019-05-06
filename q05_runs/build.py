# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data=data):

    # Write your code here
    runs=0
    lst1=data['innings'][0]['1st innings']['deliveries']
    for i,e in enumerate(lst1):
        for k in lst1[i].keys():
            player=lst1[i][k]['batsman']
            if player=='BB McCullum':
                runs+=lst1[i][k]['runs']['batsman']
        
    return(runs)


