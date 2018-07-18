# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    # Your code here
    count = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for t in deliveries:
        for m in t:
            if t[m]['batsman'] == 'RT Ponting':
                count = count + 1
    return count



