# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count=0
    for i in data['innings'][0]['1st innings']['deliveries']:
        k=list(i.values())
        if(k[0]['batsman']=='RT Ponting'):
            count= count+1
    
      

    return count





