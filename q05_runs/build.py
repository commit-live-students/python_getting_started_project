# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Your code here
    deliveries = data['innings'][0]['1st innings']['deliveries']
    
    runs = 0
    
    for x in deliveries:
        batsman = list(x.values())[0]['batsman']
        if batsman ==  'BB McCullum':
            runs += list(x.values())[0]['runs']['batsman']
    return(runs)

BC_runs(data)


