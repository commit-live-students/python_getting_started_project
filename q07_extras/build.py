# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data):

    # Write your code here
    inning1_extras = 0
    inning2_extras = 0

    difference = 0
    deliveries_1st = data['innings'][0]['1st innings']['deliveries']
    deliveries_2nd = data['innings'][1]['2nd innings']['deliveries']
    for d in deliveries_1st:
        for k, m in d.items():
            if(m.get('extras') != None):
                for e in m['extras'].values():
                    #print(e)
                    inning1_extras = inning1_extras + 1
    
    for d in deliveries_2nd:
        for k, m in d.items():
            if(m.get('extras') != None):
                for e in m['extras'].values():
                    #print(e)
                    inning2_extras = inning2_extras + 1
    
    difference = inning2_extras - inning1_extras
    return difference
#     print(inning1_extras)
#     print(inning2_extras)
extras_runs(data)




