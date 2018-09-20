# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data=data):

    # Write your code here
    runs = 0
    balls_delivered = data['innings'][0]['1st innings']['deliveries']
    for m, x in enumerate(balls_delivered):
        info = balls_delivered[m]
        for key, values in info.items():
            if info[key]['batsman'] == 'BB McCullum':
                runs += info[key]['runs']['batsman']

    return runs
BC_runs()


