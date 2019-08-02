# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for ball in deliveries:
        for each_ball in ball.values():
            if each_ball['batsman'] == 'BB McCullum':
                runs = runs + each_ball['runs']['batsman']


    return(runs)
