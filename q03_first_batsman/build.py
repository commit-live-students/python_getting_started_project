# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):
    innings = data['innings']
    deliveries_dict = innings[0]['1st innings']
    first_over = deliveries_dict['deliveries']
    first_ball = first_over[0]

    for key in first_ball:
        return first_ball[round(key,4)]['batsman']
