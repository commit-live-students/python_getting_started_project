# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    total_balls_1 = len(data['innings'][0]['1st innings']['deliveries'])
    total_balls_2 = len(data['innings'][1]['2nd innings']['deliveries'])
    extras_1 = 0
    extras_2 = 0
    list1 = []
    list2 = []
    for i in range(0, total_balls_1):
        key = next(iter(data['innings'][0]['1st innings']['deliveries'][i]))
        extras_1 = extras_1 + data['innings'][0]['1st innings']['deliveries'][i][key]['runs']['extras']
        if data['innings'][0]['1st innings']['deliveries'][i][key]['runs']['extras'] != 0:
            list1.append(data['innings'][0]['1st innings']['deliveries'][i][key]['runs']['extras'])
    
    for i in range(0, total_balls_2):
        key = next(iter(data['innings'][1]['2nd innings']['deliveries'][i]))
        extras_2 = extras_2 + data['innings'][1]['2nd innings']['deliveries'][i][key]['runs']['extras']
        
        if data['innings'][1]['2nd innings']['deliveries'][i][key]['runs']['extras'] != 0:
            list2.append(data['innings'][1]['2nd innings']['deliveries'][i][key]['runs']['extras'])
    
    print(list1)
    print(list2)
    
    #print(list1)
    difference = len(list2) - len(list1)
    return difference




