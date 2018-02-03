# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count = 0
    for delivery in data['innings'][0]['1st innings']['deliveries']:
        #print "Del: ", delivery.values()[0]['batsman'], "\n"
        if delivery.values()[0]['batsman'] == 'RT Ponting':
            count = count + 1
    return count
#print deliveries_count(data)
