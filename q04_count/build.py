# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    # Your code here
    count = 0
    delivery = data['innings'][0]['1st innings']['deliveries']
    balls = 0
    for i in range(len(delivery)):
        dely = data['innings'][0]['1st innings']['deliveries'][balls].keys()
        bats = data['innings'][0]['1st innings']['deliveries'][balls][dely[0]]['batsman']
        if bats == 'RT Ponting':
            count += 1
        balls += 1

    return count
print deliveries_count()
