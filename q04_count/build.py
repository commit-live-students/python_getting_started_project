# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    delivery=data['innings'][0]['1st innings']['deliveries']
    count=0
    for index in range(len(delivery)):
        for key in delivery[index]:
            if(delivery[index][key]['batsman']=='RT Ponting'):
                count += 1
    

    return count
data['innings'][0]['1st innings']['deliveries']


