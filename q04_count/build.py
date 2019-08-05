# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def deliveries_count(data=data):

    count = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            if delivery_info['batsman'] == 'RT Ponting':
                count += 1

    return count

ricky= deliveries_count(data)
print(ricky)


i=8

(int(8/6)+((8%6)+1)/10.0)
data['innings'][0]['1st innings']['deliveries'][8]
int(8/6)



