# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    
    first_deliveries = data['innings'][0]['1st innings']['deliveries']
    second_deliveries = data['innings'][1]['2nd innings']['deliveries']
    first_count = 0
    second_count = 0
    
    for delivery in first_deliveries:
        for key in delivery:
            
            if delivery[key]['runs']['extras'] > 0:
                first_count += 1
                
    for delivery in second_deliveries:
        for key in delivery:
            
            if delivery[key]['runs']['extras'] > 0:
                second_count += 1

    
    difference = abs(first_count - second_count)
    
    return difference

print(extras_runs())


