# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data=data):

    runs = 0
    for deliveries in data['innings'][0]['1st innings']['deliveries']:
        for key in deliveries:
            if deliveries[key]['batsman'] == "BB McCullum":
                runs += deliveries[key]['runs']['batsman']
    return(runs)
BC_runs()
