# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    delivery_list = data['innings'][0]['1st innings']['deliveries']
    count = 0
    #print (type(delivery_list))
    
    for delivery_detail in delivery_list:
        for delivery_detail_val in delivery_detail.values():
            for delivery_detail_values in delivery_detail_val:
                if(delivery_detail_values == 'batsman' and delivery_detail_val[delivery_detail_values] == 'RT Ponting'):
                    count = count + 1

    return count

deliveries_count(data)

