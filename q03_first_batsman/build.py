# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data1 = read_data()

# solution
def first_batsman(data):

    # write your code here
    name = data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']

    return name

first_batsman(data1)
