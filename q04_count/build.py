# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    # Your code here
    count = 0
    batsman = data['innings'][0]['1st innings']['deliveries']
    for rp in batsman:
        #print rp.values()[0]['batsman']
        if rp.values()[0]['batsman'] == 'RT Ponting':
            count = count + 1
    return count
#print deliveries_count()
