# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    runs = 0
    a = data['innings'][0]['1st innings']['deliveries']
    for deliveries in a:
        for b in deliveries:
            if deliveries[b]['batsman'] == 'BB McCullum':
                    runs += deliveries[b]['runs']['batsman']



    # Write your code here
    return(runs)
