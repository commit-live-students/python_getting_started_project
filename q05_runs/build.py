# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def BC_runs(data):

    # Write your code here
    runs = 0
    varfin=data['innings'][0]['1st innings']['deliveries']
    for y in varfin: 
        for v,w in y.items():
            if (w['batsman']) == 'BB McCullum':
                runs=runs+(w['runs']['batsman'])
    return(runs)



