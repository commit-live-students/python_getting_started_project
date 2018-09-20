# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def BC_runs(data = data):
   # Write your code here
    runs = 0
    innings_delivered = data['innings'][0]['1st innings']['deliveries']
    for m, x in enumerate(innings_delivered):
        dict = innings_delivered[m]
        m = m + 1
        for key,value in dict.items():
            if dict[key]['batsman'] == 'BB McCullum':
                runs += dict[key]['runs']['batsman']    
    return runs
BC_runs()








