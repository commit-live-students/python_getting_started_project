# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs = 0
    p = data['innings'][0]['1st innings']['deliveries']
    for a in p:
        for b in a:
            if (a[b]['batsman'])=='BB McCullum':
                runs += (a[b]['runs']['batsman'])
    return(runs)
BC_runs(data)


