# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data=data):

    # Write your code here
    runs=0
    for dict2 in data['innings'][0]['1st innings']['deliveries']:
        for k,v in dict2.items():
            if v['batsman']=='BB McCullum':
                runs+=v['runs']['batsman']
    return runs
                
BC_runs()
read_data()



