# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    count = 0
    balls = data['innings'][0]['1st innings']['deliveries']  
    
    for l in balls:
        for key in (l):
            if l[key]['batsman'] == 'RT Ponting':
                count+=1
    return count

            
    
deliveries_count(data)


