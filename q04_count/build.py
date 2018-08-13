# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count = 0
    deliveries_in_1st_innings = data['innings'][0]['1st innings']
    deliveries = deliveries_in_1st_innings['deliveries']
    # Your code here
    for k in deliveries:
        for i in k.values():
            if i['batsman'] =='RT Ponting':
                count+=1

    return count

deliveries_count()
