# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

#print deliveries_count()
# Your Solution Here
def deliveries_count(data=data):

    i=0;
    data1=data ['innings'][0]['1st innings']['deliveries']
    for value in data1:
        if value.values()[0]['batsman']=='RT Ponting':
            i=i+1

    count=i
    #print count
    return count
