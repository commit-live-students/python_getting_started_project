# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
name = 'name'
# Your Solution
def first_batsman(data=data):

    # Write your code here
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries:
        for key , values in delivery.items():
             if key == 0.1 :
                name = values['batsman']
        break
                
    return name
