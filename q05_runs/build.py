# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    firstinn_data=data['innings'][0]['1st innings']['deliveries']
    runs=0
    for bc in firstinn_data:
         if bc.values()[0]['batsman'] == 'BB McCullum':
                runs = runs + bc.values()[0]['runs'].values()[0]


    return(runs)
