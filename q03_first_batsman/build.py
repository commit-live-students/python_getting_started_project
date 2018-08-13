# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):

    innings = data['innings']
    first_innings = innings[0]['1st innings']
    deliveries = first_innings['deliveries']
    first_ball = deliveries[0][0.1]
    name = first_ball['batsman']

    return name
