# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    deliveries = data['innings'][0]['1st innings']['deliveries']
    return len([delivery_data for delivery_data in deliveries for delivery in delivery_data if delivery_data[delivery]['batsman'] == 'RT Ponting'])


