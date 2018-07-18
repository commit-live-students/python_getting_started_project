# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    # Your code here
    count =0
    inning = '1st innings'
    batsman_name = 'RT Ponting'
    for deliveries in data['innings'][0][inning]['deliveries']:
        for delivery in deliveries:
            if deliveries[delivery]['batsman']==batsman_name:
                count = count +1

    return count
