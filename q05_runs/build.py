# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    runs=0
    # Write your code here
    batsman=data['innings'][0]['1st innings']['deliveries']
    for i in range(0,len(batsman)):
        for j in (batsman[i].keys()):
            if batsman[i][j]['batsman']=='BB McCullum':
                runs=runs+batsman[i][j]['runs']['batsman']
    return(runs)
BC_runs(data)

