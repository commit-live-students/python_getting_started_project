# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count=0
    maintemp = (data['innings'][0]['1st innings']['deliveries'])
    len_maintemp = len(maintemp)
    
    for ctr in range(len_maintemp):
        temp_delivery=(list(maintemp[ctr]))
        delivery=float(temp_delivery[0])
       
        if maintemp[ctr][delivery]['batsman'] == 'RT Ponting':
                count+=1
    return count


