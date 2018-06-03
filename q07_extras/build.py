# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    extras_1st = 0
    for delivery in data['innings'][0]['1st innings']['deliveries']:
        keys = delivery.keys()
        for key in keys:
            if(delivery[key]['runs']['extras']):
                extras_1st +=1      
                
    extras_2nd = 0
    for delivery in data['innings'][1]['2nd innings']['deliveries']:
        keys = delivery.keys()
        for key in keys:
            if(delivery[key]['runs']['extras']):
                extras_2nd +=1      
    difference = extras_2nd - extras_1st
    return difference

extras_runs()





