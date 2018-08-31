# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs= 0
    deliv = data['innings'][0]['1st innings']['deliveries']
    for d in deliv:
        for d_num, batsm in d.items():
            if batsm['batsman'] == 'BB McCullum':
                runs+=batsm['runs']['batsman']

    return(runs)


            


