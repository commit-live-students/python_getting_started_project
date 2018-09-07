# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    # Write your code here
    st_innis = data.get('innings')[0].get('1st innings').get('deliveries')
    nd_innis = data.get('innings')[1].get('2nd innings').get('deliveries')
    
    extras_in_st_inngs = []
    extras_in_nd_inngs = []
    
    for x in range(0,len(st_innis)):
        current_delivery = st_innis[x]
        for key in current_delivery:
            extras_per_delivery = current_delivery.get(key).get('runs').get('extras')
            if extras_per_delivery != 0:
                extras_in_st_inngs.append(extras_per_delivery)
            
    
    for x in range(0,len(nd_innis)):
        current_delivery = nd_innis[x]
        for key in current_delivery:
            extras_per_delivery = current_delivery.get(key).get('runs').get('extras')
            if extras_per_delivery != 0:
                extras_in_nd_inngs.append(extras_per_delivery)
            
    difference = len(extras_in_nd_inngs)-len(extras_in_st_inngs)
    return difference

