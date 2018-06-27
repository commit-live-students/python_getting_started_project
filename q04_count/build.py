# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
lst=[]

def deliveries_count(data=data):
    lst.append(data['innings'][0]['1st innings']['deliveries'])
    
     
    # Your code here
    count = 0   
    for balls in lst:
        if {'batsman': 'RT Ponting'}:
            count += 1
        else:
            continue
        return balls
            
deliveries_count(data)
data['innings'][0]['1st innings']['deliveries']

