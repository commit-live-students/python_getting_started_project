# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data=data):
    deliveries = data['innings'][0]['1st innings']['deliveries']
    return sum([delivery_data[delivery]['runs']['batsman'] for delivery_data in deliveries for delivery in delivery_data if delivery_data[delivery]['batsman'] == 'BB McCullum'])


