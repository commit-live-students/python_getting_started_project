# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    runs = 0
    deliveries =  data['innings'][0]['1st innings'] 
    for d in deliveries['deliveries']:
        for n in d.values():
            if (n['batsman'] == 'BB McCullum'):
                runs += (n['runs']['batsman'])


    return(runs)

BC_runs(data)

