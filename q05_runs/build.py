# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def BC_runs(data):
    runs = 0
    # Write your code here
    deliveries = data['innings'][0]['1st innings']['deliveries']
    delivery_values =[d.values()[0]['runs']['batsman'] for d in deliveries if 'McCullum' in d.values()[0]['batsman'] ]
    runs = sum(delivery_values)
    return(runs)
