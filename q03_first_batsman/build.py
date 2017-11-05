# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):

    # Write your code here
    name1 = data['innings'][0]['1st innings']['deliveries'][0]
    if 0.1 in name1:
        name = name1[0.1]['batsman']





    return name
