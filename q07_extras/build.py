# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
diffrence=0
# Your Solution
def extras_runs(data=data):
    count2=0
    deliveries=data['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            if 'extras' in delivery_info:
                count2=count2+1

    deliveries=data['innings'][0]['1st innings']['deliveries']
    count1=0
    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            if 'extras' in delivery_info:
                count1=count1+1
    
    difference= count2-count1
    return difference

print(extras_runs(data))
# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
count2=0
deliveries=data['innings'][1]['2nd innings']['deliveries']
for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            if 'extras' in delivery_info:
                count2=count2+1

deliveries=data['innings'][0]['1st innings']['deliveries']
count1=0
for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            if 'extras' in delivery_info:
                count1=count1+1

                
print(count2-count1)

