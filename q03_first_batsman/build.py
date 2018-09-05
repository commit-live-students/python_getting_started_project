# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):

    first_inning = data['innings'][0]['1st innings']['deliveries']
    for deliveries in first_inning:
        for delivery in deliveries:
            name =  deliveries[delivery]['batsman']
            break
        break
    return name
