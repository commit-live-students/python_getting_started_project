# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    runs = 0
    r = data['innings'][0]['1st innings']['deliveries']
    for d in r:
        for read_inside in d:
             if d[read_inside]['batsman'] == 'BB McCullum':
                    runs = runs + d[read_inside]['runs']['batsman']




    return(runs)


