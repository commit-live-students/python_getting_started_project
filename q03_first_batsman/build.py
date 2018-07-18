# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):

    data1 = data['innings'][0]
    data2 = data1['1st innings']['deliveries'][0]
    name = data2[0.1]['batsman']
    




    return name
