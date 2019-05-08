# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    # Write your code here
    first_innings_extras = []
    seconds_innings_extras = []
    
    deliveries_1 = (data['innings'][0]['1st innings']['deliveries'])
    for d in deliveries_1:
        current_delivery = list(d)
        delivery_detail = d[current_delivery[0]]
        try:
            if(delivery_detail['extras']):
                temp1 = (list(delivery_detail['extras'].values()))
                first_innings_extras.append(temp1[0])
        except KeyError:
            pass
    
    
    
    deliveries_2 = (data['innings'][1]['2nd innings']['deliveries'])
    for d in deliveries_2:
        current_delivery = list(d)
        delivery_detail = d[current_delivery[0]]
        try:
            if(delivery_detail['extras']):
                temp2 = (list(delivery_detail['extras'].values()))
                seconds_innings_extras.append(temp2[0])
        except KeyError:
            pass
        
    difference = len(seconds_innings_extras) - len(first_innings_extras)
    
    return difference

