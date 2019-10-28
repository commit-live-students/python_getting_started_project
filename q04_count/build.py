# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    count = 0
    for deliveries in data['innings'][0]['1st innings']['deliveries']:
        for key in deliveries:
            if deliveries[key]['batsman'] == 'RT Ponting':
                count += 1
    return count
    print count

deliveries_count()
