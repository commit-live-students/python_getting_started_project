# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    x=0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for i in deliveries:
        for key,value in i.items():
            if value['batsman'] == 'BB McCullum':
                x = x + value['runs']['batsman']

    runs = x
    return(runs)
