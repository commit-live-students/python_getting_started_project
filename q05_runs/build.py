# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    runs = 0
    deliveriesInFirst = data['innings'][0]['1st innings']['deliveries']
    #print(deliveriesInFirst)
    for delivery in deliveriesInFirst:
        for ball in delivery.keys():
            batsman = delivery[ball]['batsman']
            if(batsman == 'BB McCullum'):
                runsMade = delivery[ball]['runs']['batsman']
                runs = runs + runsMade

    # Write your code here
    return runs



