# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs = 0
    for innings in data['innings']:
        for inning in innings:
            for delivery in innings[inning]['deliveries']:
                delivery_content = delivery[next(iter(delivery))]
                batsman = delivery_content['batsman']
                if (batsman == 'BB McCullum'):
                    runs += delivery_content['runs']['batsman']

    return(runs)
