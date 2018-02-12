# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    innings = data['innings'][0]
    first_innings = innings['1st innings']
    deliveries = first_innings['deliveries']
    deliveries_count = 0
    for k in deliveries:
        for key, value in k.iteritems():
            if value['batsman'] == 'RT Ponting':
                deliveries_count +=1
    return(deliveries_count)

print(deliveries_count(data))
