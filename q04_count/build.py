# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    count = 0
    innings_delivered = data['innings'][0]['1st innings']['deliveries']
    for m, x in enumerate(innings_delivered):
        dict = innings_delivered[m]
        for key,value in dict.items():
            if dict[key]['batsman'] == 'RT Ponting':
                count = count + 1
    return count
deliveries_count()


