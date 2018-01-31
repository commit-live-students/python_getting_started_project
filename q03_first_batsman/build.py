# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):
    # Write your code here
    innings =  data['innings'][0]
    first_inning = innings['1st innings']
    deliveries = first_inning['deliveries'][0]
    first_ball = deliveries[deliveries.keys()[0]]
    name = first_ball.get('batsman')
    return name
