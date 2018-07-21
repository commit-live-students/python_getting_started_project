# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def BC_runs(data):

    # Write your code here
    runs = 0
    firstinn = data['innings'][0]['1st innings']['deliveries']
    for deliv in firstinn:
        for key in deliv:
            if deliv[key]['batsman'] == 'BB McCullum':
                runs+= deliv[key]['runs']['batsman']
    return runs


