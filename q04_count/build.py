# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count = 0
    first_inning = data['innings'][0]['1st innings']['deliveries']
    for deliveries in first_inning:
        for delivery in deliveries:
            batsman_name = deliveries[delivery]['batsman']
            if batsman_name == 'RT Ponting':
                count = count + 1
            break

    return count
