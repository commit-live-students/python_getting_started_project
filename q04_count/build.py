# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    new_data = data['innings'][0]['1st innings']['deliveries']
    count = 0
    for i in new_data:
        for j,k in i.items():
            if k['batsman'] == 'RT Ponting':
                count = count + 1
    return count
