# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    runs:int = 0
    first_inning_data = data['innings'][0]['1st innings']
    deliveries = first_inning_data['deliveries']
    for delivery in deliveries:
        for index in delivery:
            if delivery[index]['batsman'] == 'BB McCullum':
                runs += delivery[index]['runs']['batsman']

    return(runs)

BC_runs(data)



