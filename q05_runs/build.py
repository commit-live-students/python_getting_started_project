# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    # Write your code here
    runs = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    print(type(deliveries))
    for d in deliveries:
        current_deliveries = list(d)
        delivery_detail = d[current_deliveries[0]]
        if(delivery_detail['batsman']== 'BB McCullum'):
            runs = runs + delivery_detail['runs']['batsman']

    return(runs)

