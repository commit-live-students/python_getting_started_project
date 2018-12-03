
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data):
    count = 0
    a = data['innings'][0]['1st innings']['deliveries']
    for deliveries in a:
        for b in deliveries:
            if deliveries[b]['batsman'] == 'RT Ponting':
                count += 1
    #print count
    return count
#deliveries_count(data)
        #for '1st innings' in 'innings':
            #print '1st innings'
            #for batsman in deliveries:
            #    count = 0
        #return(data[innings])
                #if batsman == 'RT Ponting':
                #    count += 1
                #    return(count)
                #    print count
        #print (data[batsman])
        #for batsman in deliveries:
        #count = 0
        #if batsman == 'RT Ponting':
            #count += 1
            #return(count)
                #print type(data[innings])
#print data[]'''

#deliveries_count(data)
