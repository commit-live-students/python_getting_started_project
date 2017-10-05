# Default Imports
# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs=0
    for a in data['innings']:
        for i in a:
            for b in a[i]['deliveries']:
                for k in b:
                    if b[k]['batsman'] == 'BB McCullum':
                        runs=runs+b[k]['runs']['batsman']

    return(runs)

BC_runs(data)
