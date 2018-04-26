# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()



# Your Solution
def BC_runs(data=data):

    BC_runs = data['innings'][0]['1st innings']['deliveries']
    
    runs_1 = 0   
    for i in BC_runs:
        for balls,runs in i.items():
#             print(runs['runs'])
        
            if runs['batsman'] == 'BB McCullum':
                runs_1 = runs['runs']['batsman'] + runs_1
            
    
    return runs_1
BC_runs()




