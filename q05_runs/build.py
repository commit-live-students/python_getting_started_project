# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs = 0
    for k in data['innings'][0]['1st innings']['deliveries']:
        for data['innings'][0]['1st innings']['deliveries'] in k:
            if(k[data['innings'][0]['1st innings']['deliveries']]['batsman'] == 'BB McCullum'):
                runs += k[data['innings'][0]['1st innings']['deliveries']]['runs']['batsman']
    
    return runs



