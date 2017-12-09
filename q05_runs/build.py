# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    uns = 0

    inning1 = data['innings'][0]['1st innings']['deliveries']
    for item in inning1:
        for v in item.values():
            if v['batsman'] == 'BB McCullum':
                runs = runs + v['runs']['batsman']


    return(runs)
