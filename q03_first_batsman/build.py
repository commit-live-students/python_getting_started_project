# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):
    # Write your code here
    innings =  data['innings'][0]
    first_inning = innings['1st innings']['deliveries'][0]
    first_ball = first_inning[first_inning.keys()[0]]
    name = first_ball.get('batsman')
    return name
