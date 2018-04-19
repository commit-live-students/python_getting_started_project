# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
# deliveries
    for delivery in deliveries:
         for dele in delivery.values():
            if (dele['batsman']=='BB McCullum') :
                  runs = runs + dele['runs']['batsman']  

    return(runs)

BC_runs(data)

