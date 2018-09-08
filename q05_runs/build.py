# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data=data):
    runs = 0
    dat = data['innings'][0]['1st innings']['deliveries']
    # Write your code here
    for i in list(range(len(dat))):
        for key in dat[i]:
            if  dat[i][key]['batsman'] == 'BB McCullum':
                runs = runs + dat[i][key]['runs']['batsman']
    return(runs)





