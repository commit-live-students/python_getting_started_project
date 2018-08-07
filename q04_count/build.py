# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    count=0
    for dict in data['innings'][0]['1st innings']['deliveries']:
        for value in dict.values():
            if value['batsman']=='RT Ponting':
                count+=1
        
      
            

    return count





