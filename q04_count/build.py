# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    count=0
    lst1=data['innings'][0]['1st innings']['deliveries']
    for i,e in enumerate(lst1):
        for k in lst1[i].keys():
            player=lst1[i][k]['batsman']
            if player=='RT Ponting':
                count+=1
    
    return count



