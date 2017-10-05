# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    deliveries = data['innings'][0]['1st innings']['deliveries']
    extra1 = 0
    for delivery in deliveries:
        for key , values in delivery.items():
            if( values['runs']['extras'] != 0 ):
                extra1 = extra1 + 1

    deliveries2 = data['innings'][1]['2nd innings']['deliveries']
    extra2 = 0
    for delivery in deliveries2:
        for key , values in delivery.items():
            if( values['runs']['extras'] != 0):
                extra2 = extra2 + 1

    difference = extra2 - extra1
    return difference
