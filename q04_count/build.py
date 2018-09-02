# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(deliveries_count=data):
    
    # Your code here
    count=0;
    data1=data['innings'][0]['1st innings']['deliveries'];
    for x in data1:
        for y in x:
            if (x[y]['batsman'] == 'RT Ponting'):
                count=count+1;
    print (count)
    return count;



