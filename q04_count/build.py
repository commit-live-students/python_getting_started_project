# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    count=0
    for e in data['innings'][0]['1st innings']['deliveries']:
        for key,element in e.items():
            if e[key]['batsman']== 'RT Ponting':
                count=count+1
            
    
    return count

count=0
for e in data['innings'][0]['1st innings']['deliveries']:
        for key,element in e.items():
            if e[key]['batsman']== 'RT Ponting':
                count=count+1
                print(key,e[key]['batsman'],count)

#print(data['innings'][0]['1st innings']['deliveries'])
#type(data['innings'][0]['1st innings']['deliveries'])



