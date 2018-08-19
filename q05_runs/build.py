# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def BC_runs(data):

    # Write your code here
    deliveries = list(data['innings'][0]['1st innings']['deliveries'])
    runs=0
    for delivery in deliveries:
        for deliv in delivery:
            if delivery[deliv]['batsman'] == 'BB McCullum':
                runs= runs + delivery[deliv]['runs']['batsman']

    return(runs)



