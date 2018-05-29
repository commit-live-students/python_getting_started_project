# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    runs=0
    lst1 = data['innings'][0]['1st innings']['deliveries']
    for value in lst1:
        for k2,v2 in value.items():
            if v2['batsman']  == 'BB McCullum':
                runs+=v2['runs']['batsman']
    return(runs)


