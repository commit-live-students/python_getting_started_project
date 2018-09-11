# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    count=0
    x = data['innings'][0]['1st innings']['deliveries']
    
    for i in x:
        for k in i.values():
            print(k['batsman'])
            if k['batsman'] == 'RT Ponting': 
                count = count + 1 
            
    return count

count=0
x = data['innings'][0]['1st innings']['deliveries']
for i in x:
    for k in i.values():
       print(k['batsman'])
       if k['batsman'] == 'RT Ponting': 
            count = count + 1 
print(count)


