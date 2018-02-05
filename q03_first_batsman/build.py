# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):

    batsman = data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
    return batsman
first_batsman(data)
