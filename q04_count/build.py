# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count=0
    
    a=data['innings'][0]['1st innings']['deliveries']
    # Your code here
    
    #for key,value in a.items():
     #   if a[key]['batsman']=='RT Ponting':
      #      count=count+1
    for i in range(len(a)):
        for j in a[i].values():
            if j['batsman']=='RT Ponting':
                count=count+1
    return count
    

a=deliveries_count(data)
a


