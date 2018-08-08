# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    count=0
    batsman=data['innings'][0]['1st innings']['deliveries']
#     print(batsman)
    for i in range(0,len(batsman)):
        for j in (batsman[i].keys()):
            if(batsman[i][j]['batsman']=='RT Ponting'):
                count=count+1
    return count
deliveries_count()

