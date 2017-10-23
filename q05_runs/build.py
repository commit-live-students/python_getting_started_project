# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs = 0
    for balls in data['innings'][0]['1st innings']['deliveries']:
        for key, value in balls.items():
            if value['batsman'] == 'BB McCullum':
                runs += value['runs']['batsman']

    return(runs)
