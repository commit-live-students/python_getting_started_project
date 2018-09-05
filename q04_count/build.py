# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    
    count = 0
    
    l=data['innings'][0]['1st innings']['deliveries']
    for x in l:
        for y in x:
            if(x[y]['batsman'])=='RT Ponting':
                count=count+1
    
    
    return count

                




