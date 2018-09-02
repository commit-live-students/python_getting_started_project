# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def BC_runs(data):

    # Write your code here
    runs=0;
    data1=data['innings'][0]['1st innings']['deliveries'];
    for x in data1:
        for y in x:
            if (x[y]['batsman'] == 'BB McCullum'):
                runs=runs+int(x[y]['runs']['batsman']);
                
    return(runs)



