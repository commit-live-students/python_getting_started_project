# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def deliveries_count(data = data):

#print data
    count = 0
    deli = data['innings'][0]['1st innings']['deliveries']
    for i in deli:
        #print i
        if i.values()[0]['batsman'] == 'RT Ponting':
            count = count + 1
    return (count)

deliveries_count()
