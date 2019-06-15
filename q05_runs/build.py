# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    
    # Write your code here
    runs=0
    data1=data['innings'][0]['1st innings']['deliveries']
    for i in data1:
        data2=list(i.values())
        if data2[0]['batsman']=='BB McCullum':
            if data2[0]['runs']['batsman']>0:
                runs=runs+data2[0]['runs']['batsman']

    return(runs)
BC_runs(data)

