# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    temp_1 = data.get('innings', {})
    temp_2 = temp_1[0]['1st innings']['deliveries']
    runs=0
    for t in temp_2:
        for s in t:
             if t[s]['batsman']=='BB McCullum':
                runs = runs + t[s]['runs']['batsman']
    

    return(runs)

BC_runs(data)


