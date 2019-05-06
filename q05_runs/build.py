# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    
    # Write your code here
    runs = 0
    
    for balls in data['innings'][0]['1st innings']['deliveries']:
        #print(balls[list(balls.keys())[0]])
        if balls[list(balls.keys())[0]]['batsman'] == 'BB McCullum':
            runs += balls[list(balls.keys())[0]]['runs']['batsman']
        
    
    return(runs)
BC_runs(data)

