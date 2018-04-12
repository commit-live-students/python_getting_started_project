# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data=data):
    runs=0
    maintemp = (data['innings'][0]['1st innings']['deliveries'])
    len_maintemp = len(maintemp)
    
    for ctr in range(len_maintemp):
        temp_balls=(list(maintemp[ctr]))
        balls=float(temp_balls[0])
        
        if maintemp[ctr][balls]['batsman'] == 'BB McCullum':
            runs+= int(maintemp[ctr][balls]['runs']['batsman'])

    return(runs)
print(BC_runs(data))

