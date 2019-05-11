# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    count = data['innings'][0]['1st innings']['deliveries']
    return len([x for x in count for delivery in x if x[delivery]['batsman'] == 'RT Ponting'])
    




