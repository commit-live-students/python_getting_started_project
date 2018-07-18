# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# You Solution
def extras_runs(data=data):

    # Write your code here

    deliveries1 = data['innings'][0]['1st innings']['deliveries']
    deliveries2 = data['innings'][1]['2nd innings']['deliveries']
    extras1 = []
    extras2 = []
    for t in deliveries1:
        for m in t:
            if(t[m]['runs']['extras'] > 0):
                extras1.append(t[m]['runs']['extras'])
    for t in deliveries2:
        for m in t:
            if(t[m]['runs']['extras'] > 0):
                extras2.append(t[m]['runs']['extras'])
    return abs(len(extras1)-len(extras2))



