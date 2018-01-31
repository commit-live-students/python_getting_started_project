# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    count = 0

    innings = data['innings']
    first_innings = innings[0]['1st innings']
    deliveries = first_innings['deliveries']
    
    for k in deliveries:
	for key, value in k.iteritems():
		if value['batsman'] == 'RT Ponting':
			count+=1

    return count
