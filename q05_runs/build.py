# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs=0
    deliveries=data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries:
        for key in delivery:
            if delivery[key]['batsman']=='BB McCullum':
                runs+=delivery[key]['runs']['batsman']
    return(runs)


