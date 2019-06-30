# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries:
        for ball in delivery:
            if(delivery[ball]['batsman'] == 'BB McCullum'):
                runs = runs + delivery[ball]['runs']['batsman']

    return(runs)

print(BC_runs(data))


