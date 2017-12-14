# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    data1 = data['innings'][0]['1st innings']['deliveries'][:]
    data2 = data['innings'][1]['2nd innings']['deliveries'][:]
    extras1 = 0
    for n in data1:
        if n.values()[0]['runs']['extras'] > 0:
            extras1 = extras1 + 1

    extras2 = 0
    for n in data2:
        if n.values()[0]['runs']['extras'] > 0:
            extras2 = extras2 + 1

    difference = extras2 - extras1

    return difference

print extras_runs()
print type(extras_runs())
