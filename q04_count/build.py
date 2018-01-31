# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    # Your code here
    innings =  data['innings'][0]
    deliveries = innings['1st innings']['deliveries']
    count = 0
    for i in deliveries:
        if i[i.keys()[0]].get('batsman') == 'RT Ponting':
            count +=1
    return count
