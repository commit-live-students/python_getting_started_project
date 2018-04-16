# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    # Your code here
    count = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for d in deliveries:
        current_deliveries = (list(d))
        deliveydetails = d[current_deliveries[0]]
        if(deliveydetails['batsman'])=='RT Ponting':
            count=count +1
        else:
            continue
        
    return count

