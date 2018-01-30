# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    # Your code here
    count = 0

    deliveries = data['innings'][0]['1st innings']['deliveries'] # deliveries is a list

    for delivery in deliveries:#delivery is a dictionary
        for deliv in delivery:
            dell = delivery[deliv]
            if (dell['batsman'] == 'RT Ponting'):
                count += 1
                #print dell
    #print 'Count : ', count

    return count
#deliveries_count(data)
