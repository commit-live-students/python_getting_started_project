# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    # Your code here
    subset_data = data['innings'][0]['1st innings']['deliveries']
    count = 0
    for i in subset_data:
        if i.values()[0]['batsman']=='RT Ponting':
            count=count+1
    return count
