# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs = 0
    for deliveries in data['innings'][0]['1st innings']['deliveries']:
        for data in deliveries.values():
            if data['batsman'] == 'BB McCullum':
                runs = runs + data['runs']['batsman']

    return(runs)
