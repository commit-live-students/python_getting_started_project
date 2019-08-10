# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    extras1 = 0
    extras2 = 0

    batsman1 = data['innings'][0]['1st innings']['deliveries']
    for rp in batsman1:
        if rp.values()[0]['runs']['extras'] > 0:
            extras1 = extras1 + 1

    batsman2 = data['innings'][1]['2nd innings']['deliveries']
    for rp in batsman2:
        if rp.values()[0]['runs']['extras'] > 0:
            extras2 = extras2 + 1
    difference = extras2 - extras1
    return difference
#print extras_runs()
