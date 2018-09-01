# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
runs = 0
# Your Solution
def BC_runs(data):

    # Write your code here
    total_balls = len(data['innings'][0]['1st innings']['deliveries'])
    runs = 0
    for i in range(0,total_balls):
        
        key = next(iter(data['innings'][0]['1st innings']['deliveries'][i]))
        
        if data['innings'][0]['1st innings']['deliveries'][i][key]['batsman']=='BB McCullum':
            runs = runs + data['innings'][0]['1st innings']['deliveries'][i][key]['runs']['batsman']
    
    return runs






