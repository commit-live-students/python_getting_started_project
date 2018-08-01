# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
count=0

# Your Solution Here
def deliveries_count(data=data):
    
    count = 0
    # Your code here
    dely=data['innings'][0]['1st innings']['deliveries']
    for key in dely:
        for key1, val1 in key.items():
            for key2, val2 in val1.items():
                if key2 == 'batsman':
                    if val2 == 'RT Ponting':
                        count = count + 1
                        
    
    
    return count

deliveries_count()


