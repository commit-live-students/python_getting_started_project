# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    count = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for i in deliveries:
         for delivery_no , delivery_info in i.items():
                if delivery_info['batsman']=="RT Ponting":
                    count = count+1


    return count
