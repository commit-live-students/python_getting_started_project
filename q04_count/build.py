# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count = 0
    first_inning_data = data['innings'][0]['1st innings']
    deliveries = first_inning_data['deliveries']
    for delivery in deliveries:
        for index in delivery:
            if delivery[index]['batsman'] == 'RT Ponting':
                count +=1
    return count

deliveries_count()


