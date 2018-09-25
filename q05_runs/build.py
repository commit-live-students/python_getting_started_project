# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data=data):
    
    runs = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
        
    for delivery in deliveries:
        ballIndex = list(delivery.keys())[0]
        ball = delivery[ballIndex]
        batsman = ball['batsman']
        if (batsman == 'BB McCullum'):
            runs = runs + ball['runs']['batsman']
    return(runs)


BC_runs(data)



