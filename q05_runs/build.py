# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    deliveries = data['innings'][0]['1st innings']['deliveries']  
    runs = 0
    
    for i in deliveries:
        for key in i:
            run_var = i[key]
            if run_var['batsman'] == 'BB McCullum':
                runs += run_var['runs']['batsman']
 
    return(runs)
BC_runs(data)




