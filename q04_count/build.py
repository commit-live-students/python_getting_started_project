# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count=0
    Deliveries=data['innings'][0]['1st innings']['deliveries']
    for deliveries_bowled in Deliveries:
        for delivery_bat,delivery_info in deliveries_bowled.items():
            if delivery_info['batsman'] == 'RT Ponting':
                count=count+1
   
    

    return count

from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

Deliveries=data['innings'][0]['1st innings']['deliveries']
for deliveries_bowled in Deliveries:
    for delivery_bat,delivery_info in deliveries_bowled.items():
        if delivery_info['batsman'] == 'RT Ponting':
            print(delivery_bat)



