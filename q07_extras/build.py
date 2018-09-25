# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution

def getExtras(data, inningNum):
    extra = 0
    if(inningNum == 1):
        deliveries = data['innings'][0]['1st innings']['deliveries']
    if(inningNum == 2):
        deliveries = data['innings'][1]['2nd innings']['deliveries']
    
    for delivery in deliveries:
        ballIndex = list(delivery.keys())[0]
        ball = delivery[ballIndex]
        if('extras' in ball):
            extra = extra + 1

    return extra
        
    
def extras_runs(data=data):
    difference =  abs(getExtras(data, 1) - getExtras(data, 2))    
    return difference
extras_runs(data=data)


