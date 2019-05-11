# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    deliveries = data['innings'][0]['1st innings']['deliveries']
    return sum([x[delivery]['runs']['batsman'] for x in deliveries for delivery in x if x[delivery]['batsman'] == 'BB McCullum'])

data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
 


