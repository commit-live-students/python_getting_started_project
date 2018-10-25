# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    count = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            if delivery_info['batsman'] == 'RT Ponting':
                count += 1
    

    return count

type (data)
data.keys()
(data ['innings'])
type (data ['innings'])
len (data ['innings'])
data ['innings'][0]
type(data ['innings'][0])
data['innings'][0].keys()
type(data['innings'][0]['1st innings'])

(data['innings'][0]['1st innings']).keys()
data['innings'][0]['1st innings']['deliveries']
type(data['innings'][0]['1st innings']['deliveries'])
len(data['innings'][0]['1st innings']['deliveries'])


