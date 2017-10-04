# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs = 0
    # Write your code here
    innings = data['innings']
    for inning in innings:
        for objs, values in inning.items():
            deliveries = values['deliveries']
            for delivery in deliveries:
                for delivery_number, delivery_info in delivery.items():
                    if delivery_info['batsman'] == 'BB McCullum':
                        runs += delivery_info['runs']['batsman']

    return(runs)
