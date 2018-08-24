# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
#def BC_runs(data):

    # Write your code here
def BC_runs(data):
        runs = 0
        my_list = data['innings'][0]['1st innings']['deliveries']
        for x in my_list:
            for y in x.values():
                 if y['batsman'] == 'BB McCullum':
                     runs = runs+y['runs']['batsman']
                    
        return(runs)




