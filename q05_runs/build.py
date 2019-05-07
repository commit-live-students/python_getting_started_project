# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs=0
    deliveries= data['innings'][0]['1st innings']['deliveries']
    for d in deliveries:
        for key, value in d.items():
            if value['batsman']=='BB McCullum':
                runs=runs+value['runs']['batsman']
                


    return(runs)

BC_runs(data)

