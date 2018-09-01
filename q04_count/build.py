# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):    
    # Your code here
    for i in range(len(data['innings'][0]['1st innings']['deliveries'])):
        if  data['innings'][0]['1st innings']['deliveries'][i]['batsman'] == 'RT Ponting':
            count++

    

    return count

data = read_data()
count = 0
print(data['innings'])
data = read_data()
count = 0
print(data['innings'][0]['1st innings'])

data = read_data()
count = 0

for i in range(len(data['innings'][0]['1st innings']['deliveries'])):
        if  data['innings'][0]['1st innings']['deliveries'][i]['batsman'] == 'RT Ponting':
            count=
print(count)



