# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    d=data['innings'][0]['1st innings']['deliveries']
    count=0
    for item in d:
        for v in item.values():
            for key,values in v.items():
                if key=='batsman':
                    if values=='RT Ponting':
                        count=count+1


    return count



