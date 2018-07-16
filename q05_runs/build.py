# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    innings = data['innings'][0]['1st innings']['deliveries']
    # Write your code here
    runs = 0
    for balls in innings:
        for ball in balls.values():
            if ball['batsman']=='BB McCullum':
                runs+=ball['runs']['batsman']

    return(runs)
