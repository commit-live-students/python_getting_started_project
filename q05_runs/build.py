# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs = 0
    for i in data['innings'][0]['1st innings']['deliveries']:
        innings = i
        for x in innings:
            if innings[x]['batsman'] == 'BB McCullum':
                value = innings[x]['runs']['batsman']
                runs = runs + value

    return(runs)
