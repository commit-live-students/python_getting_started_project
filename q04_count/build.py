# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data):
    
    # Your code here
    count = 0
    innings = data['innings']
    first_innings = innings[0]
    deliveries = first_innings['1st innings']['deliveries']
    for item in deliveries:
        for k, v in item.items():
            if(v['batsman'] == 'RT Ponting'):
                count += 1
    

    return count

deliveries_count(data)


