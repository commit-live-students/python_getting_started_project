# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    

    first_inning_extras = []
    second_inning_extras=[]
    
    deliveries=data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries:
        for key in delivery:
            first_inning_extras.append(delivery[key]['runs']['extras'])
            
    deliveries1=data['innings'][1]['2nd innings']['deliveries']
    for deli in deliveries1:
        for k in deli:
            second_inning_extras.append(deli[k]['runs']['extras'])
            
    first_inning_extras = [e for i, e in enumerate(first_inning_extras) if e != 0]
    second_inning_extras = [e for i, e in enumerate(second_inning_extras) if e != 0]
    difference = abs(len(first_inning_extras)- len(second_inning_extras))

    

    return difference


extras_runs()



