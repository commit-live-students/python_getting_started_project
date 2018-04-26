# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count = 0
    deliveries_count = data['innings'][0]['1st innings']['deliveries']
    
    for i in deliveries_count: 
        for deliveries,batsman in i.items():
          #  print(i)
#             print(batsman)
            if batsman['batsman'] == 'RT Ponting':
                count=count+1
    
    return count
     #return deliveries_count
deliveries_count()


