# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
count=0
ball_faced=[0]
# Your Solution Here
def deliveries_count(data=data):
    count=0
    list_deliveries= data['innings'][0]['1st innings']['deliveries']
    
    
    
    
                 
    # Your code here
    

    return count

for i in range (0,len(data['innings'][0]['1st innings']['deliveries'])):
    data['innings'][0]['1st innings']['deliveries'][i].items()
    #print(type(data['innings'][0]['1st innings']['deliveries'][i]))        
temp= data['innings'][0]['1st innings']['deliveries']
temp


