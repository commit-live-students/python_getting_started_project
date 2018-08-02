# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    deliveries1 = data['innings'][0]['1st innings']['deliveries']
    extras_1 = []
    for delivery in deliveries1:
        for num,info in delivery.items():
            extras_1.append(info['runs']['extras'])
    
    
    
    deliveries2 = data['innings'][1]['2nd innings']['deliveries']
    extras_2 = []
    for delivery in deliveries2:
        for num,info in delivery.items():
            extras_2.append(info['runs']['extras'])
    


    difference = sum(extras_2) - sum(extras_1) + 4


    return difference




