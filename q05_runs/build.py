# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    
    l=(data['innings'][0]['1st innings']['deliveries'])
    c=0
    for x in l:
        for y in x:
            if(x[y]['batsman'])=='BB McCullum':
                c+=(x[y]['runs']['batsman'])
                    

    # Write your code here

    runs=c
    return(runs)






