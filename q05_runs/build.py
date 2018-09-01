# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    dta = data['innings'][0]['1st innings']['deliveries']
    runs = 0
    for i in range(len(dta)):
        key = list(dta[i].keys())[0]
        if dta[i][key]['batsman'] == 'BB McCullum':
            runs = dta[i][key]['runs']['batsman'] + runs
    return(runs)

dta = data['innings'][0]['1st innings']['deliveries']
runs = 0
#print(dta)
print(dta[0])


