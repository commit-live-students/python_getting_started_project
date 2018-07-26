# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def BC_runs(data):

    runs = 0 
    balls = data['innings'][0]['1st innings']['deliveries']
    for l in balls:
        for key in (l):
            if l[key]['batsman'] == 'BB McCullum':
                runs += l[key]['runs']['batsman']
    return runs
BC_runs(data)








