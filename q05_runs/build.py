# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
data['innings'][0]['1st innings']['deliveries'][0].values()#[0.1]['batsman']

# runs = 0
# for deli in data['innings'][0]['1st innings']['deliveries']:
#     for val in deli.values():
#         if val['batsman'] == 'BB McCullum':
#             runs += val['runs']['batsman']
# runs            
# Your Solution
def BC_runs(data):

#     # Write your code here
    runs = 0
    for deli in data['innings'][0]['1st innings']['deliveries']:
        for val in deli.values():
            if val['batsman'] == 'BB McCullum':
                runs += val['runs']['batsman']
   

    return(runs)



