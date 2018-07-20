# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs=0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for t in deliveries:
        for m in t:
            if t[m]['batsman'] == 'BB McCullum' :
                runs+=t[m]['runs']['batsman']

            

    return(runs)



