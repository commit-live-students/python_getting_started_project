# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    deliveries = data['innings'][0]['1st innings']['deliveries']
    deliveryCount = 0
    for each_delivery in deliveries:
        for deliveryNumber, deliveryInfo in each_delivery.items():
            if deliveryInfo['batsman'] == 'RT Ponting':
                deliveryCount += 1
    return deliveryCount
