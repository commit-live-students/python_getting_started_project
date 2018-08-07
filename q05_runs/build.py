# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs=0
    for dict in data['innings'][0]['1st innings']['deliveries']:
        
        for value_dict in dict.values():
            if value_dict['batsman']=='BB McCullum':
                runs+=value_dict['runs']['batsman']


    return(runs)





