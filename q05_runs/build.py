# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    runs = 0 
    deliveries_delivered = data['innings'][0]['1st innings']['deliveries']
    for x in deliveries_delivered:
        for y in x:
            if x[y]['batsman'] == 'BB McCullum':
                
              runs+= x[y]['runs']['batsman']
                

    return(runs)

BC_runs(data)


